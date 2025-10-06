import os
import argparse
import requests
from image_downloader import download_image


def fetch_spacex_launch(launch_id=None):
    os.makedirs('images', exist_ok=True)
    if launch_id is None:
        launch_id = 'latest'

    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url)
    response.raise_for_status()

    launch = response.json()
    images = launch['links']['flickr']['original']

    for i, image_url in enumerate(images):
        filename = f'spacex_{i}.jpg'
        download_image(image_url, f'images/{filename}')
        print(f'Скачано: {filename}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Скачать фото SpaceX')
    parser.add_argument('--launch_id', help='ID запуска')
    args = parser.parse_args()

    fetch_spacex_launch(args.launch_id)