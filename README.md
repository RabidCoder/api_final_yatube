# API для Yatube

Учебный проект Яндекс.Практикум курса Python-разработчик(backend).

## Описание

Yatube - социальная сеть для публикации дневников. Позволяет публиковать посты, комментировать посты, осуществлять подписку на авторов.

Для разработки API использован Django REST framework.

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/yandex-praktikum/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

## Документация к API

 После запуска dev-сервера документация к API доступна по адресу:
 <http://127.0.0.1:8000/redoc/>

## Примеры запросов

### Публикация и получение комментариев к постам

Request:```[GET] http://127.0.0.1:8000/api/v1/posts/1/comments/```

Response:

```json
[
    {
        "id": 1,
        "author": "string",
        "post": 1,
        "text": "string",
        "created": "2022-08-06T10:59:31.721673Z"
    }
]
```

Request:```[POST] http://127.0.0.1:8000/api/v1/posts/1/comments/```

Request body:

```json
{
    "text": "1st comment"
}
```

Response:

```json
{
    "id": 1,
    "author": "string",
    "post": 1,
    "text": "string",
    "created": "2022-08-06T10:59:31.721673Z"
}
```

### Публикация и получение постов

Request: ```[GET] http://127.0.0.1:8000/api/v1/posts/?limit=2&offset=1```

Response:

```json
{
    "count": 5,
    "next": "http://127.0.0.1:8000/api/v1/posts/?limit=2&offset=3",
    "previous": "http://127.0.0.1:8000/api/v1/posts/?limit=2",
    "results": [
        {
            "id": 2,
            "author": "string",
            "text": "string",
            "pub_date": "2022-08-06T10:01:17.273956Z",
            "image": "string",
            "group": 0
        },
        {
            "id": 3,
            "author": "string",
            "text": "string",
            "pub_date": "2022-08-06T10:42:39.095878Z",
            "image": "string",
            "group": 0
        }
    ]
}
```

Request: ```[POST] http://127.0.0.1:8000/api/v1/posts/```

Request body:

```json
{
    "text": "string",
    "image": "string",
    "group": 0
}
```

Response:

```json
{
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2022-08-06T10:59:31.721673Z",
    "image": "string",
    "group": 0
}
```

## Автор

 Александр Кречетов (krechet0v.alex@yandex.ru)