## Описание проекта:

Проект представляет собой RESTful API для социальной сети YATUBE
Возможности: создание поста, комментирование поста, объединять посты в группы, подписываться на авторов

### Технологии
- Python 3.7
- Django 3.2
- Django REST Framework
- Simple JWT

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/yandex-praktikum/api_final_yatube
```

```
cd yatube_api
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

## Примеры запросов к API

### Получение токена авторизации

```
POST /api/v1/jwt/create/
```

Тело запроса:
```json
{
    "username": "Pavel",
    "password": "password"
}
```

Ответ:
```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

### Публикация поста

```
POST /api/v1/posts/
```

Заголовки:
```
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...
Content-Type: application/json
```

Тело запроса:
```json
{
    "text": "Текст поста",
    "group": 1
}
```

Ответ:
```json
{
    "id": 1,
    "author": "Pavel",
    "text": "Текст поста",
    "pub_date": "2025-04-12T14:39:53.270628Z",
    "image": null,
    "group": 1
}
```