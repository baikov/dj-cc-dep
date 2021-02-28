import requests
from pathlib import Path

width = [20, 40, 80, 160, 320, 640, 1280, 2560]
bitmap = ['png', 'jpg', 'webp']
vector = ['svg', 'ai', 'pdf', 'eps']
cdn = 'https://flagcdn.com'
save_to_path = 'flags/media/national-flags'


def get_flag_img(iso2):
    iso2 = iso2.lower()
    for format in bitmap:
        for size in width:
            url = f'{cdn}/w{size}/{iso2}.{format}'
            dest = f'{save_to_path}/{iso2}/w{size}'
            Path(dest).mkdir(parents=True, exist_ok=True)
            r = requests.get(url)
            with open(f'{dest}/{iso2}.{format}', "wb") as f:
                f.write(r.content)

    for format in vector:
        url = f'{cdn}/{iso2}.{format}'
        dest = f'{save_to_path}/{iso2}'
        Path(dest).mkdir(parents=True, exist_ok=True)
        r = requests.get(url)
        with open(f'{dest}/{iso2}.{format}', "wb") as f:
            f.write(r.content)
