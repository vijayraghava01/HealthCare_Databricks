from healthcare_data_platform.common.exceptions import ValidationException


def validate_required_columns(df, required_columns):

    missing = []

    for column in required_columns:

        if column not in df.columns:

            missing.append(column)

    if missing:

        raise ValidationException(
            f"Missing required columns : {missing}"
        )

    return True