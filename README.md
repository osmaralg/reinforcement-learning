# reinforment-learning

.. image::  /static/assets/img/caputure.JPG

Install
==============

Install the virtualenv package

`pip install virtualenv`

Create virtual environment called env, myenv, etc. 

`virtualenv env`

Activate the virtualenvironmnent (LInux)

`source env/bin/activate`

Go the path of the project and install the required libraries 

`pip install -r requirements.txt`

Testing
-----------------
To run the server in the localhost run 

`python manage.py runserver`

Open your browser in the address localhost:8000 


File Description
-----------------
project_emec2.py: Takes input from the reinforcement learning model and creates the necessary JSON files for further visualization.

manage.py: Contains all the commands required to run the server

manage - Copy.py:

requirements.txt: Contains all library requirements to run the server

articles\admin.py: Registers the models.

articles\apps.py: 

articles\functions.py: Contains general functions used by other scripts in the repository.

articles\models.py:

articles\views.py:

articles\templates: Contains HTML scripts required for the dashboard

static: Contains Javascrips, CSS, Highcharts code and other files required for the dashboard

static\data\RL Model: Contains scripts for the reinfocement learning model

django_project:Contains Python scripts and other files required for the dashboard




