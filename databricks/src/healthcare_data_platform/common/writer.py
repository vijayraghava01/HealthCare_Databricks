def write_bronze(
        df,
        checkpoint,
        table_name):

    return (
        df.writeStream
          .format("delta")
          .option(
              "checkpointLocation",
              checkpoint
          )
          .trigger(availableNow=True)
          .toTable(table_name)
    )