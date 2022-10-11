import pandas as pd


def infer_gender(row):
    if row["Title"] == "Mr":
        return "male"
    elif row["Title"] in ["Mrs", "Ms"]:
        return "female"
    else:
        raise ValueError(f'Invalid Title: {row["Title"]}')


def find_daily_hours_watched(row):
    monthly_hours = row["Monthly_number_of_hours_watched"]
    if monthly_hours < 0 or monthly_hours > 744:
        raise ValueError("Monthly_number_of_hours_watched must be between 0 to 744, inclusive")
    return round(row["Monthly_number_of_hours_watched"] / 30, 2)


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
