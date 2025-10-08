import os
import argparse
import requests
from image_downloader import download_image


def fetch_spacex_launch(launch_id='latest'):
    os.makedirs('images', exist_ok=True)

    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url)
    response.raise_for_status()

    launch = response.json()
    image_urls = launch['links']['flickr']['original']

    for image_number, image_url in enumerate(image_urls):
        filename = f'spacex_{image_number}.jpg'
        download_image(image_url, f'images/{filename}')
        print(f'Скачано: {filename}')


def main():
    parser = argparse.ArgumentParser(description='Скачать фото SpaceX')
    parser.add_argument('--launch_id', default='latest', help='ID запуска')
    args = parser.parse_args()

    fetch_spacex_launch(args.launch_id)

if __name__ == '__main__':
    main()