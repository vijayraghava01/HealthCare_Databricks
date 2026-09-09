from healthcare_data_platform.common.exceptions import (
    ValidationException
)


class ValidationManager:

    @staticmethod
    def validate(df, config):

        if df is None:

            raise ValidationException(
                "DataFrame is None."
            )

        if not df.columns:

            raise ValidationException(
                "DataFrame contains no columns."
            )

        return True