import pandas as pd

from src.constants import CSVColumns, Gender


def infer_gender(row):
    title = row[CSVColumns.title.value]
    if title == "Mr":
        return Gender.male.value
    elif title in ["Mrs", "Ms"]:
        return Gender.female.value
    else:
        raise ValueError(f'Invalid Title: {title}')


def find_daily_hours_watched(row):
    monthly_hours = row[CSVColumns.monthly_hours.value]
    if monthly_hours < 0 or monthly_hours > 744:
        raise ValueError(f"{CSVColumns.monthly_hours.value} must be between 0 to 744, inclusive")
    return round(row[CSVColumns.monthly_hours.value] / 30, 2)


def apply_transformation(transform_func, df, column_name, update_column=True):
    new_rows = []
    for idx, row in df.iterrows():
        value = transform_func(row)
        if update_column:
            new_row = {
                **row.to_dict(),
                column_name: value
            }
        else:
            new_row = row.to_dict()
        new_rows.append(new_row)
    new_data_frame = pd.DataFrame(new_rows)
    return new_data_frame
