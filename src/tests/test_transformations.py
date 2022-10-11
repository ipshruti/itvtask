import pandas as pd
import pytest

from src.constants import CSVColumns, Gender
from src.transformations import infer_gender, find_daily_hours_watched, apply_transformation

INFER_GENDER_DF = pd.DataFrame(data=[
    {CSVColumns.title.value: "Mr"},
    {CSVColumns.title.value: "Mrs"},
    {CSVColumns.title.value: "Ms"},
])

MONTHLY_HOURS_DF = pd.DataFrame(data=[
    {CSVColumns.monthly_hours.value: 230.9},
    {CSVColumns.monthly_hours.value: 34.54},
    {CSVColumns.monthly_hours.value: 720},
])

MONTHLY_AND_DAILY_HOURS_DF = pd.DataFrame(data=[
    {
        CSVColumns.monthly_hours.value: 230.9,
        CSVColumns.daily_hours.value: 7.7
    },
    {
        CSVColumns.monthly_hours.value: 34.54,
        CSVColumns.daily_hours.value: 1.15
    },
    {
        CSVColumns.monthly_hours.value: 720,
        CSVColumns.daily_hours.value: 24.0
    },
])


@pytest.mark.parametrize(
    "title,gender",
    [
        ("Mr", Gender.male.value),
        ("Mrs", Gender.female.value),
        ("Ms", Gender.female.value),
    ]
)
def test_infer_gender(title, gender):
    assert infer_gender({CSVColumns.title.value: title}) == gender


def test_infer_gender_raise_error_for_invalid_title():
    with pytest.raises(ValueError) as exc:
        infer_gender({CSVColumns.title.value: "INVALID"})
    assert str(exc.value) == "Invalid Title: INVALID"


def test_find_daily_hours_watched():
    assert find_daily_hours_watched({CSVColumns.monthly_hours.value: 345.45}) == 11.51


@pytest.mark.parametrize(
    "hours", [-0.1, 744.1]
)
def test_find_daily_hours_watched_invalid_no_of_hours(hours):
    with pytest.raises(ValueError) as exc:
        find_daily_hours_watched({CSVColumns.monthly_hours.value: hours})
    assert str(exc.value) == f"{CSVColumns.monthly_hours.value} must be between 0 to 744, inclusive"


@pytest.mark.parametrize(
    "df,transform_func,column_name,update_column,expected_df",
    [
        (INFER_GENDER_DF, infer_gender, CSVColumns.title.value, False, INFER_GENDER_DF),
        (
                MONTHLY_HOURS_DF,
                find_daily_hours_watched,
                CSVColumns.daily_hours.value,
                True,
                MONTHLY_AND_DAILY_HOURS_DF
        ),
    ]
)
def test_apply_transformation(
        df,
        transform_func,
        column_name,
        update_column,
        expected_df
):
    transformed = apply_transformation(
        transform_func=transform_func,
        df=df,
        column_name=column_name,
        update_column=update_column
    )
    pd.testing.assert_frame_equal(transformed, expected_df)
