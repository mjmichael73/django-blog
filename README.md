### Django commands:

    django-admin startproject blog
    python manage.py migrate
    python manage.py runserver
    python manage.py runserver --settings=blog.settings
    python manage.py startapp cms
    python manage.py shell
    python manage.py makemigrations cms
    python manage.py migrate
    python manage.py sqlmigrate cms 0001 (Before migrating you can run this command to see the actual sql query)
    python manage.py createsuperuser
    
### Superuser:

    Username: admin
    Email: admin@example.com
    Password: password