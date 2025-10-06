import requests
import os
from urllib.parse import urlsplit


def download_image(url, path):
    response = requests.get(url)
    response.raise_for_status()

    with open(path, 'wb') as file:
        file.write(response.content)


def get_file_extension(url):
    path = urlsplit(url).path
    return os.path.splitext(path)[1]