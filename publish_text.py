import os
import requests
from dotenv import load_dotenv


def publish_text_to_channel(bot_token, channel_id, text):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

    payload = {
        'chat_id': channel_id,
        'text': text,
        'parse_mode': 'HTML'
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        data = response.json()

        if data['ok']:
            print("Текст успешно опубликован в канал!")
            print(f"ID сообщения: {data['result']['message_id']}")
        else:
            print(f"Ошибка: {data['description']}")


    except requests.exceptions.RequestException as e:
        print(f"Ошибка при отправке запроса: {e}")


def main():
    load_dotenv()

    TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    TELEGRAM_CHANNEL_ID = os.getenv('TELEGRAM_CHANNEL_ID')

    text = """ Добро пожаловать в космический канал!

Здесь мы публикуем самые удивительные фотографии космоса:
• Изображения далеких галактик
• И многое другое!

Следите за обновлениями! """

    publish_text_to_channel(TELEGRAM_BOT_TOKEN, TELEGRAM_CHANNEL_ID, text)

if __name__ == '__main__':
    main()