from pyspark.sql import DataFrame

from healthcare_data_platform.config.constants import (
    CATALOG,
    BRONZE_SCHEMA,
    LANDING_VOLUME,
    SCHEMA_VOLUME
)


class BronzeReader:

    @staticmethod
    def read_stream(spark,dataset_config) -> DataFrame:

        landing_path = (
            f"/Volumes/{CATALOG}/"
            f"{BRONZE_SCHEMA}/"
            f"{LANDING_VOLUME}/"
            f"{dataset_config['landing_path']}"
        )

        schema_path = (
            f"/Volumes/{CATALOG}/"
            f"{BRONZE_SCHEMA}/"
            f"{LANDING_VOLUME}/"
            f"{SCHEMA_VOLUME}/"
            f"{dataset_config['landing_path']}"
        )
        reader = (
                        spark.readStream
                            .format("cloudFiles")

                            .option(
                                "cloudFiles.format",
                                "csv"
                            )

                            .option(
                                "header",
                                "true"
                            )

                            .option(
                                "cloudFiles.inferColumnTypes",
                                "true"
                            )

                            .option(
                                "cloudFiles.schemaLocation",
                                schema_path
                            )

                            .option(
                                "cloudFiles.schemaEvolutionMode",
                                "addNewColumns"
                            )

                           
                            .option(
                                "rescuedDataColumn",
                                "_rescued_data"
                            )
                    )

        schema_hints = dataset_config.get(
                        "schema_hints"
                    )

        if schema_hints:

                        reader = reader.option(
                            "cloudFiles.schemaHints",
                            schema_hints
                        )

        return reader.load(
            landing_path
        )