import os
from pathlib import Path
from .models import Tag

def load_svg() -> dict:
    BASE_DIR = Path(__file__).parent.parent
    data = {}

    icon_dir = os.path.join(BASE_DIR, f'staticfiles/main/img/icon/')
    if os.path.exists(icon_dir):
        icon_files_name = [f for f in os.listdir(icon_dir) if os.path.isfile(os.path.join(icon_dir, f))]
        for f in icon_files_name:
            if f.endswith(".svg"):
                with open(os.path.join(icon_dir, f), 'r', encoding='utf-8') as icon:
                    data['_'.join(f.split('.svg')[0].split('-'))] = icon.read()

    return data

def get_tags():
    tags = Tag.objects.all()

    return tags.order_by('-usage_count')