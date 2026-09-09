# ===========================
# Unity Catalog
# ===========================

CATALOG = "healthcare_catalog"

BRONZE_SCHEMA = "bronze"
SILVER_SCHEMA = "silver"
GOLD_SCHEMA = "gold"


# ===========================
# Volumes
# ===========================

LANDING_VOLUME = "landing_volume"
CHECKPOINT_VOLUME = "bronze_checkpoints"
SCHEMA_VOLUME = "bronze_schema"

LANDING_VOLUME_PATH = (
    f"/Volumes/{CATALOG}/{BRONZE_SCHEMA}/{LANDING_VOLUME}"
)

CHECKPOINT_VOLUME_PATH = (
    f"/Volumes/{CATALOG}/{BRONZE_SCHEMA}/{LANDING_VOLUME}/{CHECKPOINT_VOLUME}"
)

SCHEMA_VOLUME_PATH = (
    f"/Volumes/{CATALOG}/{BRONZE_SCHEMA}/{LANDING_VOLUME}/{SCHEMA_VOLUME}"
)


# ===========================
# Monitoring
# ===========================

AUDIT_SCHEMA = "monitoring"

PIPELINE_NAME = "bronze_ingestion"


# ===========================
# Metadata Columns
# ===========================

INGESTION_TIME = "_ingestion_timestamp"

SOURCE_FILE = "_source_file"

SOURCE_PATH = "_source_path"