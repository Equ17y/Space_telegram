import sys
import time
import random
import argparse
import os
import requests
from dotenv import load_dotenv

try:
    import imghdr
except ImportError:
    class FakeImghdr:
        @staticmethod
        def what(file, h=None): return None


    sys.modules['imghdr'] = FakeImghdr()

def main():
    load_dotenv()
    telegram_api_key = os.environ['TELEGRAM_BOT_TOKEN']
    chat_id = os.environ['TELEGRAM_CHANNEL_ID']

    parser = argparse.ArgumentParser(description='Publishes space images in the telegram channel.')
    parser.add_argument('post_delay', help='Posting frequency in hours', type=float, nargs='?', default=4)
    post_delay = parser.parse_args().post_delay

    image_paths = []
    for address, dirs, files in os.walk('images'):
        for name in files:
            if name.startswith(('nasa_apod_', 'spacex', 'nasa_epic_')):
                image_paths.append(os.path.join(address, name))

    max_image_size = 20 * 1024 * 1024
    sec_per_hour = 3600

    while True:
        random.shuffle(image_paths)
        for image_path in image_paths:
            if not os.path.isfile(image_path): continue
            if os.path.getsize(image_path) > max_image_size: continue

            url = f"https://api.telegram.org/bot{telegram_api_key}/sendPhoto"
            with open(image_path, 'rb') as f:
                files = {'photo': f}
                data = {'chat_id': chat_id}
                response = requests.post(url, files=files, data=data)
                response.raise_for_status()

            time.sleep(sec_per_hour * post_delay)

if __name__ == '__main__':
    main()