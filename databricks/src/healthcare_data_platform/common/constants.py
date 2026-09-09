from pyspark.sql.functions import current_timestamp

# Catalog
CATALOG = "healthcare_catalog"

# Schemas
BRONZE_SCHEMA = "bronze"
SILVER_SCHEMA = "silver"
GOLD_SCHEMA = "gold"

# Volume
LANDING_VOLUME = "landing_volume"

# Audit Column Names
INGESTION_TIME = "_ingestion_timestamp"
SOURCE_FILE = "_source_file"
LOAD_DATE = "_load_date"

# Checkpoint Root
CHECKPOINT_ROOT = "/Volumes/healthcare_catalog/bronze/landing_volume/checkpoints"