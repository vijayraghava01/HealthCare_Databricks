import os
from pathlib import Path
from dotenv import load_dotenv

# Find project root .env
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_FILE = BASE_DIR / ".env"

load_dotenv(ENV_FILE)


AZURE_STORAGE_CONNECTION_STRING = os.getenv(
    "AZURE_STORAGE_CONNECTION_STRING"
)

CONTAINER_NAME = "landing"

VOLUME_ROOT = (
    "/Volumes/healthcare_catalog/"
    "bronze/landing_volume"
)


# logger.info("Current directory: %s", os.getcwd())
# logger.info("Python: %s", os.sys.executable)

# logger.info(
#     "ENV file loaded: %s",
#     ENV_FILE.exists()
# )

# logger.info(
#     "Azure connection exists: %s",
#     AZURE_STORAGE_CONNECTION_STRING is not None
# )