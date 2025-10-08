import os
import requests
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHANNEL_ID = os.getenv('TELEGRAM_CHANNEL_ID')


def publish_text_to_channel():

    text = """ Добро пожаловать в космический канал!

Здесь мы публикуем самые удивительные фотографии космоса:
• Изображения далеких галактик
• И многое другое!

Следите за обновлениями! """

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

    payload = {
        'chat_id': TELEGRAM_CHANNEL_ID,
        'text': text,
        'parse_mode': 'HTML'
    }

    try:
        response = requests.post(url, json=payload)
        data = response.json()

        if data['ok']:
            print("Текст успешно опубликован в канал!")
            print(f"ID сообщения: {data['result']['message_id']}")
        else:
            print(f"Ошибка: {data['description']}")

    except Exception as e:
        print(f"Ошибка: {e}")


def main():
    publish_text_to_channel()

if __name__ == '__main__':
    main()