from healthcare_data_platform.common.logger import get_logger

logger = get_logger()


def start_ingestion():
    logger.info(
        "Bronze ingestion started."
    )