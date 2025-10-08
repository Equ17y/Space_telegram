import os
import argparse
import requests
from dotenv import load_dotenv
from image_downloader import download_image, get_file_extension


def fetch_apod(api_key, count=5):
    os.makedirs('images', exist_ok=True)
    url = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': api_key, 'count': count}

    response = requests.get(url, params=params)
    response.raise_for_status()

    for apod_number, apod_data in enumerate(response.json()):
        if apod_data['media_type'] != 'image':
            continue

        extension = get_file_extension(apod_data['url']) or '.jpg'
        filename = f'nasa_apod_{apod_number}{extension}'
        download_image(apod_data['url'], f'images/{filename}')
        print(f'Скачано: {filename}')


def main():
    load_dotenv()
    api_key = os.environ['NASA_API_KEY']

    parser = argparse.ArgumentParser(description='Скачать APOD фото NASA')
    parser.add_argument('--count', type=int, default=5, help='Количество фото')
    args = parser.parse_args()

    fetch_apod(api_key, args.count)

if __name__ == '__main__':
    main()