def read_csv_autoloader(spark,source_path,schema_location):
    return(
         spark.readStream
            .format("cloudFiles")
            .option("cloudFiles.format", "csv")
            .option("header", "true")
            .option(
                "cloudFiles.schemaLocation",
                schema_location
            )
            .load(source_path)
    )
    