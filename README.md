# Космические фото. Телеграм.
Бот для автоматической публикации космических изображений в Telegram-канал.


## Как установить
Клонируйте репозиторий:
```bash
git clone https://github.com/Equ17y/Space_telegram.git
cd space_images_bot
```
Создайте виртуальное окружение и установите зависимости:
```bash
python -m venv venv
venv\scripts\activate
pip install -r requirements.txt
```

Создайте файл .env и добавьте переменные окружения:

- NASA_API_KEY=токен NASA API необходимо получить на сайте [NASA API APOD](https://api.nasa.gov/).
- TELEGRAM_BOT_TOKEN=your_telegram_bot_token
- TELEGRAM_CHANNEL_ID=@your_channel_username

## Основные скрипты

**fetch_spacex_images.py**  
Скачивает фото запуска ракет SpaceX с помощью [SpaceX API](https://github.com/r-spacex/SpaceX-API). В качестве аргумента скрипт принимает в командной строке id запуска. Если id не указать, то скачаются фото последнего запуска, если они есть. Пример запуска:
```
python fetch_spacex_images.py 
```

**fetch_nasa_apod_images.py**  
Скачивает фото на космическую тематику с сайта [NASA API APOD](https://api.nasa.gov/#apod). Чтобы воспользоваться NASA API необходимо получить токен NASA_API_KEY. Пример запуска:
```
python fetch_nasa_apod_images.py
```
**fetch_nasa_epic_images.py**  
Скачивает фото планеты Земля с сайта [NASA API EPIC](https://api.nasa.gov/#epic). Чтобы воспользоваться скриптом необходима та же настройка с токеном, что и в скрипте выше. Пример запуска:
```
python fetch_nasa_epic_images.py
```
**publish_images.py**  
Публикует в телеграм канале фотографии, скачанные с помощью скриптов выше.
Далее создать канал, где будут публиковаться фотографии, и добавить туда бота в качестве администратора.
Ссылку на канал в формате @name добавить в переменную TG_CHANNEL_NAME. Пример запуска:

```
python publish_images.py          # каждые 4 часа
python publish_images.py 2        # каждые 2 часа  
python publish_images.py 24       # раз в сутки
```

**publish_one_image.py**  
Публикует в телеграм канале указанную фотографию. Пример запуска:
```
python publish_one_image.py images\spacex_1.jpg
```