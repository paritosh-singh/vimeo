## About the project
This project get vimeo users using Vimeo API. The database server used is MySql. The users are fetched using Vimeo API
and are stored in database. The user's name, username, vimeo url, is staffpick, is paying and has uploaded is stored in
database. For now 5000 users are fetched from vimeo and stored in database,

## Dependencies
* Python 2.7
* Django 1.5
* mysql-python
* requests 0.14.0

All dependencies are already included in project


## Project Setup
* Clone the project from git.
* Open your terminal.
* Goto project directory.
* Create your mysql database.
* Change database settings in settings.py in (vimeo_assignment/settings.py)

## Loading schema in database
For loading schema in database run the command
>>> python manage.py syncdb

## Crawl vimeo users to your Mysql DB
For crawling vimeo users run the command
>>> python manage.py fetch_vimeo_users
This task fetches 5000 vimeo users and take 2.5 hours (approx). Incase you want to fetch less users change "USERS_LIMIT"
in settings.py(vimeo_assignment/settings.py).

## Running the application
* For running the application run the command
>>> python manage.py runserver
* Go to your browser and hit the url "http://127.0.0.1:8000"
* Now enter your search term and press enter.
* Also to apply filters, click on corresponding filters.

