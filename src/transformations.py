import pandas as pd

from src.constants import CSVColumns, Gender


def infer_gender(row):
    """
    Transform function to infer gender from the row
    :param row: A row of a pandas DataFrame
    :return: Returns the gender: male, female
    """
    title = row[CSVColumns.title.value]
    if title == "Mr":
        return Gender.male.value
    elif title in ["Mrs", "Ms"]:
        return Gender.female.value
    else:
        raise ValueError(f'Invalid Title: {title}')


def find_daily_hours_watched(row):
    """
    Transform function to add a column for daily watched hours,
    which is calculated from monthly watched hours by dividing that
    by 30.
    :param row:
    :return:
    """
    monthly_hours = row[CSVColumns.monthly_hours.value]
    if monthly_hours < 0 or monthly_hours > 744:
        raise ValueError(f"{CSVColumns.monthly_hours.value} must be between 0 to 744, inclusive")
    return round(row[CSVColumns.monthly_hours.value] / 30, 2)


def apply_transformation(transform_func, df, column_name, update_column=True):
    """
    Given a transform function it will apply the transformation to all the
    rows of the given dataframe, by adding or updating the given
    column name if `update_column` flag is true
    :param transform_func: Given transformation function
    :param df: pd.DataFrame to apply transformation on
    :param column_name: column_name to add/update in the dataframe
    :param update_column: Will add/update column_name id this flag is True.
    :return: Transformed DataFrame
    """
    # Rows of the new DataFrame
    new_rows = []
    # Iterated dataframe rows
    for idx, row in df.iterrows():
        # Apply given transformation to each row.
        value = transform_func(row)
        # update column only if update_column flag is True
        if update_column:
            new_row = {
                **row.to_dict(),
                column_name: value
            }
        else:
            new_row = row.to_dict()
        # Add row to the new_rows list
        new_rows.append(new_row)
    # Create new transformed DataFrame from new rows
    new_data_frame = pd.DataFrame(new_rows)
    return new_data_frame
