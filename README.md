 If you want to get  source you have to clone the repository:

```bash
https://github.com/serg-lubeshko/TestAccounting.git
```

Once you have the sources, you can run it in docker. 

```bash
docker-compose up --build
```

Method 2 run application. Enter commands in sequence

```
python manage.py makemigrations
python manage.py migrate
# Fill in db. Create Superuser (username: admin password: admin)
python manage.py datapp  
python manage.py runserver  

```

To start mailing, you need to enter the command. Mail for  purposes will not come to email, because  'django.core.mail.backends.console.EmailBackend' is connected with output to the console (The application also provides celery)

Attention! Newsletters come for the previous day, so look at the date of the transaction

```
python manage.py send_email
```



Go to address

```
http://127.0.0.1:8000/

```

To work with the application, you need to follow  link in swagger. Enter username and password (example: admin/admin). Get access token and then login

```
/b-login/
```

