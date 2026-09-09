from pyspark.sql.functions import (
    current_timestamp,
    current_date,
    col
)

def add_audit_columns(df):

    return (
        df
        .withColumn(
            "_ingestion_timestamp",
            current_timestamp()
        )
        .withColumn(
            "_load_date",
            current_date()
        )
        .withColumn(
            "_source_file",
            col("_metadata.file_name")
        )
    )