# api_final
api final

### Как запустить проект:

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

### Описание

Здесь вы можете совершать определенные действия с обьектами:

| Endpoint | Object | Methods | Description |
| --- | :---: | :---: | --- |
| `/api/v1/posts/` | Post | GET, POST | Получаем все посты или создаем пост. |
| `/api/v1/posts/{id}/` | Post | GET, PUT, PATCH, DELETE | Получаем, редактируем, заменяем, удаляем пост. |
| `/api/v1/posts/{post_id}/comments/` | Comment | GET, POST | Получаем все комментарии конкретного поста или создаем комментарий. |
| `/api/v1/posts/{post_id}/comments/{id}/` | Comment | GET, PUT, PATCH, DELETE | Получаем, редактируем, заменяем, удаляем комментарий. |
| `/api/v1/groups/` | Group | GET | Получаем все группы (только чтение). |
| `/api/v1/groups/{id}/` | Group | GET | Получаем данные группы (только чтение). |
| `/api/v1/follow/` | Follow | GET, POST | Получаем все подписки пользователя, сделавшего GET запрос, или подписываемся на другого пользователя. |
| `/api/v1/jwt/create/` | Token | POST | Получаем токен. |
| `/api/v1/jwt/refresh/` | Token | POST | Обновляем токен. |
| `/api/v1/jwt/verify/` | Token | POST | Проверяем токен. |

### Примеры

POST запрос `/api/v1/posts/`
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
Ответ:
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2022-09-21T19:57:45.329Z",
  "image": "string",
  "group": 0
}
```
