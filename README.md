# Movies

A simple movies website.

### Quickstart

Get the source from GitHub:

    git clone https://gitlab.com/ipandzic/rtomatoes/

Create Python2 virtual environment:

    virtualenv  myenv
    . myenv/bin/activate

Install required files:

    pip install -r requirements.txt

Migrate the database:

    python manage.py migrate

Create super user:

    python manage.py createsuperuser

Run development server:

    python manage.py runserver

Point your browser to http://127.0.0.1:8000/admin and login

Running tests:

    python manage.py test