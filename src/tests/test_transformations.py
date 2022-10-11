import pytest

from src.transformations import infer_gender, find_daily_hours_watched


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
