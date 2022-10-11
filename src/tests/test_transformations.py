import pandas as pd
import pytest

from src.transformations import infer_gender, find_daily_hours_watched, apply_transformation

INFER_GENDER_DF = pd.DataFrame(data=[
    {"Title": "Mr"},
    {"Title": "Mrs"},
    {"Title": "Ms"},
])

MONTHLY_HOURS_DF = pd.DataFrame(data=[
    {"Monthly_number_of_hours_watched": 230.9},
    {"Monthly_number_of_hours_watched": 34.54},
    {"Monthly_number_of_hours_watched": 720},
])

MONTHLY_AND_DAILY_HOURS_DF = pd.DataFrame(data=[
    {
        "Monthly_number_of_hours_watched": 230.9,
        "daily_number_of_hours_watched": 7.7
    },
    {
        "Monthly_number_of_hours_watched": 34.54,
        "daily_number_of_hours_watched": 1.15
    },
    {
        "Monthly_number_of_hours_watched": 720,
        "daily_number_of_hours_watched": 24.0
    },
])


@pytest.mark.parametrize(
    "title,gender",
    [
        ("Mr", "male"),
        ("Mrs", "female"),
        ("Ms", "female"),
    ]
)
def test_infer_gender(title, gender):
    assert infer_gender({"Title": title}) == gender


def test_infer_gender_raise_error_for_invalid_title():
    with pytest.raises(ValueError) as exc:
        infer_gender({"Title": "INVALID"})
    assert str(exc.value) == "Invalid Title: INVALID"


def test_find_daily_hours_watched():
    assert find_daily_hours_watched({"Monthly_number_of_hours_watched": 345.45}) == 11.51


@pytest.mark.parametrize(
    "hours", [-0.1, 744.1]
)
def test_find_daily_hours_watched_invalid_no_of_hours(hours):
    with pytest.raises(ValueError) as exc:
        find_daily_hours_watched({"Monthly_number_of_hours_watched": hours})
    assert str(exc.value) == "Monthly_number_of_hours_watched must be between 0 to 744, inclusive"


@pytest.mark.parametrize(
    "df,transform_func,column_name,update_column,expected_df",
    [
        (INFER_GENDER_DF, infer_gender, "Title", False, INFER_GENDER_DF),
        (
                MONTHLY_HOURS_DF,
                find_daily_hours_watched,
                "daily_number_of_hours_watched",
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
