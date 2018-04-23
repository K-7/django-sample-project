# django-sample-project
Python 2.7 used

### Setup Instructions

Clone the repo

```sh
git clone git@github.com:K-7/django-sample-project.git
```

Install dependecies

```sh
pip install -r requirements.txt
```

Database setup

*   Create a Postgress database in the name 'marlo'
*   Run the migrate command mentioned below for database schema creation
*   Run the setup command mentioned below for dummy data to be loaded into database
*   Start the server using runserver command

```sh
python manage.py migrate
python manage.py setup
python manage.py runserver
```

Run Testcases.

```sh
python manage.py test
```