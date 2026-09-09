from pyspark.sql.streaming import StreamingQuery

from healthcare_data_platform.config.constants import (
    CATALOG,
    BRONZE_SCHEMA,
    CHECKPOINT_VOLUME,
    LANDING_VOLUME
)


class BronzeWriter:

    @staticmethod
    def write_stream(
        df,
        dataset_config
    ) -> StreamingQuery:

        table_name = (
            f"{CATALOG}."
            f"{BRONZE_SCHEMA}."
            f"{dataset_config['target_table']}"
        )

        checkpoint_path = (
            f"/Volumes/{CATALOG}/"
            f"{BRONZE_SCHEMA}/"
            f"{LANDING_VOLUME}/"
            f"{CHECKPOINT_VOLUME}/"
            f"{dataset_config['landing_path']}"
        )

        query = (
            df.writeStream

            .format("delta")

            .option(
                "checkpointLocation",
                checkpoint_path
            )

            .option(
                "mergeSchema",
                "true"
            )

            .trigger(
                availableNow=True
            )

            .toTable(
                table_name
            )
        )

        return query