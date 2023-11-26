Проект (курсовая)  "бэкенд-часть SPA веб-приложения"
В проекте на основе Django REST framework реализована бэкенд-часть веб-приложения трекера привычек по книге Джеймса Клира «Атомные привычки».

Запуск :
1. Клонирование репозитория
git clone https://github.com/Xarveister/drf_course_work
2. Установка зависимостей
Создать виртуальное окружение:

python -m venv venv
Активировать виртуальное окружение:

venv\Scripts\activate.bat  для Windows
source venv/bin/activate  для Linux и MacOS
Установить зависимости:

pip install -r requirements.txt
3. Установка и запуск Redis
Установка:

sudo apt-get install redis-server
Запуск:

redis-server --port 6380 --slaveof 127.0.0.1 6379
4. Установка и настройка PostgreSQL
Установка:

sudo apt-get install postgresql
Запуск:

psql -U postgres
Создание базы данных, где atomic_habits - название базы данных, которое можно изменить в файле .env

CREATE DATABASE coursework;
Закрыть PostgreSQL:

\q
5. Создание телеграм-бота и получение API-ключа
Для создания Telegram-бота найдите в чате самого главного бота:

https://t.me/BotFather
Начните с ним диалог и выберите команду создания нового бота:

/newbot  # create a new bot
Введите имя вашего бота, которое отображается пользователям.

Введите юзернейм вашего бота - это уникальный идентификатор, по которому бота можно будет найти. Также важно, чтобы имя заканчивалось на _bot

Если имя подходит под все правила, BotFather предоставит API-ключ (токен) и полезные ссылки для использования бота

6. Настройка переменных окружения
В папке config/ создать файл .env, в который записать свои данные:
DB_NAME=
DB_USER_PASSWORD=
TELEGRAM_BOT_API_KEY=
TELEGRAM_CHAT_ID=
7. Применение миграций
python manage.py migrate
8. Запуск сервера Django
python manage.py runserver
9. Запуск сервиса периодических задач CELERY осуществляется в разных терминалах двумя командами
python.exe -m celery -A config worker -l INFO -P eventlet 
celery -A config beat -l INFO -S django  