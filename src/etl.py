import pandas as pd

from src.transformations import apply_transformation, infer_gender, find_daily_hours_watched


DATA_FILE = "data/sample.csv"
OUTPUT_FILE = "data/output.csv"


def main():
    df = pd.read_csv(DATA_FILE)
    df_gender_inferred = apply_transformation(
        transform_func=infer_gender,
        df=df,
        column_name="Title",
        update_column=False
    )
    df_with_daily_hours = apply_transformation(
        transform_func=find_daily_hours_watched,
        df=df_gender_inferred,
        column_name="daily_number_of_hours_watched",
    )
    df_with_daily_hours.to_csv(OUTPUT_FILE, index=False)


if __name__ == '__main__':
    main()
