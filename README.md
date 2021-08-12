# Интерактивная карта города с интересными местами, их фото и описанием.
![](gif/preview_map.gif)

# Стек:
Python 3, Django 3, SQLite

# Описание:
Интерактивная карта Москвы, на которую можно например добавить локации для активного отдыха с подробными описаниями и комментариями. Чем-то похожим занимается Яндекс.Афиша.

# Установка:
Для запуска сайта вам понадобится Python третьей версии.

Склонируйте проект из реппозитория:


    git clone https://github.com/wiky-avis/where_to_go.git


Установите виртуальное окружение:

    python -m venv venv

Активируйте виртуальное окружение:

    source venv/Scripts/activate

Установите необходимые зависимости:

    pip install -r requirements.txt

Запустите миграции базы данных:

    python manage.py migrate

Создайте суперпользователя:

    python manage.py createsuperuser

Запустите проект:

    python manage.py runserver

Доступ в админку http://127.0.0.1:8000/admin/.

    
## Дополнительные возможности:

Наполнение базы тестовыми данными:

    python manage.py load_place

