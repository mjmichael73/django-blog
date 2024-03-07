## Django Blog

### Features:
    - Admin panel (default django admin panel)
    - FullTextSearch on posts using PostgreSQL
    - RSS
    - Sitemap
    - ...

### Requirements:

    - docker and docker compose
    - python 3.12.2
    - Django 5.0.2


### Get the project up and running on your system:

    Run postgres: docker comopse up --build -d
    Create virtualenv: python -m virtualenv venv
    Install dependencies: cd /be/blog -> pip install -r requirements.txt
    Run DB migration: cd /be/blog -> python manage.py migrate
    Create superuser: python manage.py createsuperuser
    Run the server: python manage.py runserver
    
    

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
    python manage.py dumpdata --indent=2 --output=blog_data.json
    python -Xutf8 manage.py dumpdata --indent-2 --output=blog_data.json
    python manage.py loaddata blog_data.json
    
### Superuser:

    Username: admin
    Email: admin@example.com
    Password: password

### Docker commands:

    docker compose up --build -d
    docker compose down --remove-orphans --volumes
    docker compose logs -f django-blog-db
    docker compose ps


### TODO:
    - ?