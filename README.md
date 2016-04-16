# GakktuServer

GakktuServer provides a API for the Immigrant/Refugee application Gakktu í bæinn.

## Installation

Clone the project from here
`git clone https://github.com/fortena/GakktuServer.git`


## Optional virtualenv

A virtual environment is recommended.
Install it with pip if you don't already have it.
`pip install virtualenv`

Create a virtual environment e.g.
`virtualenv gs -p python3.4`

Source the virtualenv
`source gs/bin/activate`

## Install requirements and migrate database

CD into GakktuServer and install requirements inside the virtualenv
`pip install -r requirements.txt`

Migrate the database
`python manage.py makemigrations`
`python manage.py migrate`

## Run the server locally

In the terminal type
`python manage.py runserver`

Now the server should be running locally on port 8000

## Create a django user for access and authenticaion

In the terminal type
`python manage.py createsuperuser`
