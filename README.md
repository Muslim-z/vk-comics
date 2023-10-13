# Как загружать комиксы из интернета и публиковать их на стене группы ВКонтакте

Этот код загружает комиксы из интернета и публикует их на стене группы ВКонтакте. Для работы с кодом необходимо установить библиотеки `requests` и `python-dotenv`.

## Как установить

1. Скачайте код из репозитория.
2. Установите зависимости командой `pip install -r requirements.txt`.
3. Создайте файл `.env` в корневой директории проекта.
4. Добавьте в файл `.env` следующие переменные окружения:
    ```
    VK_ACCESS_TOKEN=ваш_токен
    VK_GROUP_ID=айди_вашей_группы
    ```
5. Запустите код командой `python main.py`.

## Как использовать

1. Запустите код командой `python main.py`.
2. Код загрузит случайный комикс с сайта [xkcd.com](https://xkcd.com/) и опубликует его на стене группы ВКонтакте.

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и web-разработке на сайте [Devman](https://dvmn.org/).