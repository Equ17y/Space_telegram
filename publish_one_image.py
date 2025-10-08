import os
import random
import requests
from dotenv import load_dotenv

def main():
    load_dotenv()
    telegram_api_key = os.environ['TELEGRAM_BOT_TOKEN']
    chat_id = os.environ['TELEGRAM_CHANNEL_ID']

    images = [f for f in os.listdir('images') if f.startswith(('nasa_apod_', 'spacex', 'nasa_epic_'))]

    random_image = random.choice(images)
    image_path = os.path.join('images', random_image)

    print(f"Публикую: {random_image}")

    url = f"https://api.telegram.org/bot{telegram_api_key}/sendPhoto"

    with open(image_path, 'rb') as f:
        photo_content = f.read()

    files = {'photo': photo_content}
    data = {'chat_id': chat_id}
    response = requests.post(url, files=files, data=data)
    response.raise_for_status()

if __name__ == '__main__':
    main()