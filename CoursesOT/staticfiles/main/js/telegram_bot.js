const BACKEND_URL = "{{ BACKEND_URL }}"; 

function constructDataCheckString(initData) {
    const params = new URLSearchParams(initData);
    const dataObj = {};
    for (const [key, value] of params.entries()) {
        dataObj[key] = value;
    }

    const receivedHash = dataObj.hash;

    delete dataObj.hash;

    const sortedKeys = Object.keys(dataObj).sort();
    const dataCheckString = sortedKeys.map(key => `${key}=${dataObj[key]}`).join("\n");

    return { dataCheckString, receivedHash };
}

async function sendUserDataToBackend(dataCheckString, receivedHash) {
    const tg = window.Telegram.WebApp;

    if (tg.initDataUnsafe && tg.initDataUnsafe.user) {

        const requestBody = {
            data_check_string: dataCheckString,
            received_hash: receivedHash,
            auth_data: tg.initData
        };

        const response = await fetch(`${BACKEND_URL}/api/create-session/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(requestBody)
        });

        const data = await response.json();
        
        if (data.status === "success" && data.redirect_url) {
            window.location.href = data.redirect_url;
        } else {
            console.error("Auth error: ", data)
            window.location.href = `${data.redirect_url}?message=${data.message}&status=${data.code}`;
        }
    } else {
        console.error("Telegram data not found!")
    }
}

async function controlUserData() {
    const tg = window.Telegram.WebApp;

    if (!tg.initData) {
        window.location.href = `/error?message=initData+is+missing!&status=400`;
        console.error("initData is missing!");
        return
    }

    const { dataCheckString, receivedHash } = constructDataCheckString(tg.initData);

    await sendUserDataToBackend(dataCheckString, receivedHash);
}

controlUserData();