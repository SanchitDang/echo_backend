# Echo Backend

## admin creds for django panel
url: /master-admin
admin@admin.com
admin

python manage.py makemigrations
python manage.py migrate 

python manage.py runserver 0.0.0.0:8000

## After  flutter web build
-> Change base href="/" in index.html to base href="/login-user/"