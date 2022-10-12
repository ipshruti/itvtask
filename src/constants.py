from enum import Enum


class CSVColumns(Enum):
    """Columns of the input CSV that we have used in the code"""
    title = "Title"
    monthly_hours = "Monthly_number_of_hours_watched"
    daily_hours = "daily_number_of_hours_watched"


class Gender(Enum):
    male = "male"
    female = "female"


DATA_FILE = "data/sample.csv"
OUTPUT_FILE = "data/output.csv"
