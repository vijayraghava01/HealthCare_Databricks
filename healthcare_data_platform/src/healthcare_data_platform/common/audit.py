from datetime import datetime

from healthcare_data_platform.common.logger import get_logger

logger = get_logger()


def audit(message):

    logger.info(
        f"{datetime.utcnow()} | {message}"
    )