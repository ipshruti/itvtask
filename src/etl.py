import click as click
import pandas as pd

from src.constants import CSVColumns, DATA_FILE, OUTPUT_FILE
from src.transformations import apply_transformation, infer_gender, find_daily_hours_watched


@click.command()
@click.option('--input-csv', default=DATA_FILE, help='Path of input csv')
@click.option('--output-csv', default=OUTPUT_FILE, help='Path to save the output csv')
def main(input_csv, output_csv):
    """
    Main entrypoint for using the CLI to run the full pipeline
    with all the transformations. This will run the pipeline
    and save the out in the output csv.
    :param input_csv: input csv to extract and transform
    :param output_csv: path to save the final csv
    :return: None
    """
    df = pd.read_csv(input_csv)
    df_gender_inferred = apply_transformation(
        transform_func=infer_gender,
        df=df,
        column_name=CSVColumns.title.value,
        update_column=False
    )
    df_with_daily_hours = apply_transformation(
        transform_func=find_daily_hours_watched,
        df=df_gender_inferred,
        column_name=CSVColumns.daily_hours.value
        ,
    )
    df_with_daily_hours.to_csv(output_csv, index=False)


if __name__ == '__main__':
    main()
