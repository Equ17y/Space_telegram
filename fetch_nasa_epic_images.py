import argparse
import os
import requests
from dotenv import load_dotenv
from image_downloader import download_image


def fetch_epic(api_key, count=None):
    os.makedirs('images', exist_ok=True)
    params = {'api_key': api_key}

    # Получаем последнюю дату
    response = requests.get('https://api.nasa.gov/EPIC/api/natural/all', params=params)
    response.raise_for_status()

    latest_date = response.json()[0]['date']
    date_formatted = latest_date.replace('-', '/')

    # Получаем фото за эту дату
    response = requests.get(f'https://api.nasa.gov/EPIC/api/natural/date/{latest_date}', params=params)
    response.raise_for_status()

    epic_images = response.json()
    if count:
        epic_images = epic_images[:count]

    for image_number, image_data in enumerate(epic_images):
        image_url = f'https://api.nasa.gov/EPIC/archive/natural/{date_formatted}/png/{image_data["image"]}.png'
        filename = f'nasa_epic_{image_number}.png'
        download_image(image_url, f'images/{filename}')
        print(f'Скачано: {filename}')


def main():
    load_dotenv()
    api_key = os.environ['NASA_API_KEY']

    parser = argparse.ArgumentParser(description='Скачать EPIC фото Земли')
    parser.add_argument('--count', type=int, help='Количество фото')
    args = parser.parse_args()

    fetch_epic(api_key, args.count)

if __name__ == '__main__':
    main()