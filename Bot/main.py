import asyncio
import logging
import os
from pathlib import Path
from dotenv import load_dotenv, set_key
from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo
from aiogram.enums import ParseMode
from pyngrok import ngrok



BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / '.env'
load_dotenv(ENV_PATH)

BOT_TOKEN = os.getenv('BOT_TOKEN')

WEB_APP_URL = ngrok.connect(8000).public_url
set_key(ENV_PATH, 'WEB_APP_URL', WEB_APP_URL)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message()
async def start_command(message: types.Message):
    web_button = types.InlineKeyboardButton(
        text='🌐 Open Web App', web_app=WebAppInfo(url=WEB_APP_URL)
    )
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[[web_button]]
    )

    await message.answer('Click the button for open web application:', reply_markup=keyboard)

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
