# Описание приложения

Запуск проекта.
 - Скопировать проект с помощью ``` git clone https://github.com/iNgredie/Simbirsoft_spring_practicum.git ```
 - ```docker-compose up --build ```  собрать приложение и сделать его первоначальный запуск
 - ```docker-compose down -v``` – остановить работу приложения
 - ```docker-compose run web python manage.py migrate``` – сделать необходимые миграции
 - ```docker-compose up``` – окончательно запустить приложение.

Стек технологий и требований к ним для реализации веб-приложения 

- Python 3
- Django 
- СУБД PostgreSQL (через отдельный Docker-образ)
- Контейнер с приложением должен использовать alpine
- Описание API - Swagger OpenAPI Version 3

---
- Swagger достпупен по ссылке: ```http://localhost:8000/swagger```   
 -   ``` http://localhost:8000/auth/users/``` регистрация пользователя через post запрос  
 ``` 
{
    "username": "username",
    "email": "example@email.com",
    "password": "yourpassword"
}
 ```

- После этого на вашу почту, указанную при регистрации придет с ссылкой  
```activate/{uid}/{token}```
- ``` http://localhost:8000/auth/users/activation/``` подтверждение регистрации, необходимо отправить
 post запрос с вашим uid и token:   
```
{
    "uid": "MTE",
    "token": "ahr1ny-d6b4fc662e1bbf6f7d8f4dddacaf63fb"
}
```

- Получение токена: post запрос на  ```http://localhost:8000/auth/token/login/```
```
{
    "email": "example@email.com",
    "password": "yourpassword"
}
``` 
- Создание JWT токена: post запрос на ```http://localhost:8000/auth/jwt/create/```
```
{
    "email": "example@email.com",
    "password": "yourpassword"
}
```

- Создать пользователя можно командой :```python manage.py create_user -h```, посмотреть необходимые префиксы и уже создать пользователя с нужными параметрами.

```Тестовое задание для группового практикума Python Simbirsoft```
