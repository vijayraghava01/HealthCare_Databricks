import pandas as pd


class DataValidator:

    @staticmethod
    def check_duplicates(df: pd.DataFrame, column: str):

        duplicates = df[df.duplicated(column)]

        if not duplicates.empty:
            raise ValueError(
                f"Duplicate values found in {column}"
            )

    @staticmethod
    def check_nulls(df: pd.DataFrame, column: str):

        if df[column].isnull().any():
            raise ValueError(
                f"Null values found in {column}"
            )

    @staticmethod
    def check_row_count(df: pd.DataFrame, expected: int):

        if len(df) != expected:
            raise ValueError(
                f"Expected {expected}, got {len(df)}"
            )