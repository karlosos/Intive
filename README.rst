Intive cognitive
====================

Machine learning prediction of salary data from `salary.csv` using linear regression.
Presentation on web application using django.

.. image:: https://i.imgur.com/QvDwJs0.png

Installation
===============

Clone this repo with `git clone https://github.com/karlosos/Intive`

Usage
===============

Launch server with `python manage.py runserver`. Navigate to http://127.0.0.1:8000/.

Functionality:
================

Django web application
------------------------

Index view
^^^^^^^^^^^^^^^^

Default page which contains form for filtering salaries. Form can be used to defining range of working years and range of salaries. This form sends data using POST to `salary_filter_view`.

Salary view
^^^^^^^^^^^^^^^^

Shows salaries data which is stored in database. To show this view navigate to *http://127.0.0.1:8000/salary/* url or click *Salary data* in the menu. 

This shows all the data in table and creates interactive chart using `jchart`.

View is defined in `salary_view` function.

Salary filtered view
^^^^^^^^^^^^^^^^^^^^^^

It shows salaries from given range based on user input from form. It has the same functionality like salary view but display only limited data.

Salary prediction
^^^^^^^^^^^^^^^^^^^^^

Predicting salaries using `python calculate_salaries.py` which is using `salary.csv` as data source and saving output to `salary_predicted.csv`.

Data import from csv to db
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Import data from `salary_predicted.csv` to existing `db.sqlite3` using `python import_csv_to_sqlite`

Used libraries
===================

1. django 2.1.5 - web framework
2. django-jchart - rendering charts
3. pandas
4. sklearn - linear regression

What can be done
=============================

1. Write tests (especially for filtering)
2. I don't like that salary_view and salary_filter_view are doing basically the same thing. There's redundancy
3. Deploy application to heroku
