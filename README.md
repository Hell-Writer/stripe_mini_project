# Stripe-mini-project

# Описание
Это тестовое задание по работе со Stripe

# Установка:

## - Склонируйте репозиторий

## - Создайте и активируйте виртуальное окружение (win)

python -m venv venv

source venv/scripts/activate

## - Установите библиотеки из requirements.txt
python -m pip install --upgrade pip

pip install -r requirements.txt

## - Проведите миграции
python manage.py makemigrations

python manage.py migrate

## - Запустите сервер
python manage.py runserver
