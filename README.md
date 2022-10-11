# ITV Task

# Installation

- Create a Python Virtualenv on Python 3.9
- Install requirements

```bash
pip install -r requirements.txt
```

- Run ETL pipeline

```bash
PYTHONPATH='.' python src/etl.py --input-csv data/sample.csv --output-csv data/output.csv
```

You can pass your csv using the `input-csv` parameter. A sample csv has been provided
in `data/sample.csv` for quick testing.

# Running tests

We use `pytest` for running tests. Running tests is as easy as running the following command:

```bash
pytest -v
```

# Problem Statement

## Question 1 : Bash Scripting

You want to write a script that automates the deployment and tests of a data product in an
AWS environment. The code used for the data product is versioned control in github and the
repository called viewing_product has the following structure:

```
_viewing_product
|__scr
   |__main.py
   |__helpers.py
|__test
   |__ __init__.py
   |__ viewing_product_test.py
|__README.md
```

### Write a bash script that will do the following:

- Checkout the github repository
- Run the python test
- Zip the repository
- Save the zip bundle to a S3 bucket called s3://data_product_artefact under the suffix
  viewing_product

## Question 2 : Unit testing

One of your data pipelines is defined as follows:

```
+-----------------+     +------------------+     +------------------+      +----------------+
| Load a csv file |     |                  |     |                  |      |                |
|     from S3     | --> | Transformation 1 | --> | Transformation 2 | -->  | Store as a csv |
|                 |     |                  |     |                  |      |                |
+-----------------+     +------------------+     +------------------+      +----------------+
```

### The csv file contains the following columns:
 
- User_id - integer - length 10
- Title - string - Possible values [Mrs, Mr, Ms]
- Age - int - length up to 3
- Monthly_number_of_hours_watched - decimal with 2 digit precision - from 0.00 to
  744 (24 hour per day for 31 days)


### Transformations

The 1st transformation takes the title and infer the gender of the users:
 
- If Mrs or Ms return female
- If Mr return male
  
The 2nd transformation creates an additional column called 
“daily_number_of_hours_watched” by dividing the Monthly_number_of_hours_watched by 30

### Task:

- a) Write a python function for each transformation and test them (unit testing) using the module of your choice.
- b) Create 1 slide where you explain how you will perform end to end testing for this pipeline
