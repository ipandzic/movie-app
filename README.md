# Movies

This is a simple Django website displaying movies opening this week gathered from https://www.rottentomatoes.com/browse/opening/. In creating this website, I used Python 2.7.12 and Django 1.11. For more details see requirements.txt.

### Quickstart

Get the source from GitHub:

    git clone https://gitlab.com/ipandzic/rtomatoes/

Create Python2 virtual environment:

    virtualenv myenv
    . myenv/bin/activate

Install required files:

    pip install -r requirements.txt

Migrate the database:

    python manage.py migrate

Use the custom manage.py command to populate the database using data from www.rottentomatoes.com/browse/opening/:

    python manage.py transfer


Create super user:

    python manage.py createsuperuser

Run development server:

    python manage.py runserver

Point your browser to http://127.0.0.1:8000/core to browse the website, to http://127.0.0.1:8000/admin to login into the admin interface or go to http://127.0.0.1:8000/api to use the API.
