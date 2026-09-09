from pyspark.sql.functions import current_timestamp,col



class MetadataManager:

    @staticmethod
    def add_metadata(df):

        return (

            df

            .withColumn(
                "_ingestion_timestamp",
                current_timestamp()
            )

            .withColumn(
                "_source_file",
                col("_metadata.file_name")
            )

        )