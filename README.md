# ITV Task

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
  The 1st transformation takes the title and infer the gender of the users :
- If Mrs or Ms return female
- If Mr return male
  The 2nd transformation creates an additional column called
  “daily_number_of_hours_watched” by dividing the Monthly_number_of_hours_watched by
  30
  a) Write a python function for each transformation and test them (unit testing) using the
  module of your choice.
  b) Create 1 slide where you explain how you will perform end to end testing for this
  pipeline
