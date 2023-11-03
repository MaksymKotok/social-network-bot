## Installation

```bash
pip install -r req.txt
```

## Starting the Social Network

```bash
python3 manage.py migrate
python3 manage.py runserver
```

## Starting the Automated Bot

```bash
python3 bot/script.py
```

You can update the ```config.json``` in the ```bot``` folder to change settings of the bot.

```json
{
    "number_of_users": 4,
    "max_posts_per_user": 3,
    "max_likes_per_user": 7,
    "sign_up_url": "http://127.0.0.1:8000/auth/users/",
    "auth_url": "http://127.0.0.1:8000/auth/jwt/create/",
    "post_url": "http://127.0.0.1:8000/post/"
}
```

## ENDPOINTS

User Sign Up
```bash
POST http://127.0.0.1:8000/auth/users/
```

User Login (JWT Token)
```bash
POST http://127.0.0.1:8000/auth/jwt/create/
```

Post Creation
```bash
POST http://127.0.0.1:8000/post/
```

Post Like
```bash
POST http://127.0.0.1:8000/post/{post_id}/like/
```

Post Unike
```bash
DELETE http://127.0.0.1:8000/post/{post_id}/like/
```

Analytics about likes on a post (Available only as a superuser)
```bash
GET http://127.0.0.1:8000/analytics/post/?date_from=2023-11-01&date_to=2023-11-03
```

Analytics about user activity (Available only as a superuser)
```bash
GET http://127.0.0.1:8000/analytics/user/activity/
```

## Postman Collection
You can find postman collection in the root folder of a repo. Please, enjoy!
