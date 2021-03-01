import requests
from pathlib import Path
import os


def delete_img(file):
    os.remove(file)


def download_img(url, path, name):
    file = f'{path}/{name}'
    Path(path).mkdir(parents=True, exist_ok=True)
    r = requests.get(url)
    with open(file, 'wb') as f:
        f.write(r.content)


def get_flag_img(iso2):
    width = [20, 40, 80, 160, 320, 640, 1280, 2560]
    bitmap = ['png', 'jpg', 'webp']
    vector = ['svg', 'ai', 'pdf', 'eps']
    cdn = 'https://flagcdn.com'
    save_to_path = 'flags/media/national-flags'
    iso2 = iso2.lower()
    for format in bitmap:
        for size in width:
            url = f'{cdn}/w{size}/{iso2}.{format}'
            dest = f'{save_to_path}/{iso2}/w{size}'
            file_name = f'{dest}/{iso2}.{format}'
            download_img(url, dest, file_name)

    for format in vector:
        url = f'{cdn}/{iso2}.{format}'
        dest = f'{save_to_path}/{iso2}'
        file_name = f'{dest}/{iso2}.{format}'
        download_img(url, dest, file_name)


def get_historical_flag_img(url, from_year, to_year, country_iso2):
    iso2 = country_iso2.lower()
    path = f'flags/media/historical-flags/{iso2}'
    file_name = f'{iso2}-{from_year}-{to_year}.svg'
    download_img(url, path, file_name)

    return f'{iso2}/{file_name}'
