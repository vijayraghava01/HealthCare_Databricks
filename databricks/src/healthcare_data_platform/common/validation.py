def validate_not_empty(df):

    if df.isEmpty():
        raise Exception(
            "No records found."
        )