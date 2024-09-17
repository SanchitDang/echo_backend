# Echo Backend

## super user creds for django panel
url: /master-admin
email: admin@admin.com
username: admin
pass: 123456

## admin creds user mgmt
url: /login-admin
email: admin@admin.com
username: admin
pass: 123456

## user cred
url: /login-user
email: demo@demo.com / test@test.com
username: demo / test
pass: 123456

### create super user
py manage.py createsuperuser

### migrations
python manage.py makemigrations
python manage.py migrate 

### runserver
python manage.py runserver 0.0.0.0:8000

## After flutter web build
-> Change base href="/" in index.html to base href="/login-user/"