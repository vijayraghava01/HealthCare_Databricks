from pyspark import pipelines as dp  # type: ignore

from healthcare_data_platform.bronze.metadata import MetadataManager
from healthcare_data_platform.bronze.validation import ValidationManager
from healthcare_data_platform.bronze.reader import BronzeReader
from healthcare_data_platform.config.bronze_datasets import BRONZE_DATASETS


def create_bronze_table(dataset_name, config):

    # if dataset_name == "appointments":

    #     @dp.table(
    #         name=config["target_table"],
    #         comment=f"Bronze table for {dataset_name}",
    #     )
    #     @dp.expect_or_fail(
    #         "TEST - appointments intentionally fails",
    #         "1 = 0",
    #     )
    #     def bronze_table():

    #         df = BronzeReader.read_stream(
    #             spark,  # type: ignore
    #             config,
    #         )

    #         df = MetadataManager.add_metadata(df)

    #         ValidationManager.validate(
    #             df,
    #             config,
    #         )

    #         return df

    # else:

    @dp.table(
            name=config["target_table"],
            comment=f"Bronze table for {dataset_name}",
        )
    def bronze_table():

            df = BronzeReader.read_stream(
                spark,  # type: ignore
                config,
            )

            df = MetadataManager.add_metadata(df)

            ValidationManager.validate(
                df,
                config,
            )

            return df

    return bronze_table


for dataset_name, config in BRONZE_DATASETS.items():

    create_bronze_table(
        dataset_name,
        config,
    )
