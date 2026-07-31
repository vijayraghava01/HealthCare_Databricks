# Databricks notebook source

# COMMAND ----------

from healthcare_data_platform.common.logger import get_logger
from healthcare_data_platform.common.validation import validate_required_columns

logger = get_logger()

logger.info("Bronze ingestion started")

# COMMAND ----------

df = spark.read.option("header", "true").csv("...") # type: ignore

# COMMAND ----------

validate_required_columns(
    df,
    [
        "Claim_ID",
        "Patient_Name",
        "Insurance_Payment"
    ]
)

# COMMAND ----------

logger.info("Validation successful")