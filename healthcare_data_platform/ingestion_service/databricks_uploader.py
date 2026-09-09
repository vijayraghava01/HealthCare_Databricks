from databricks.sdk import WorkspaceClient

from ingestion_service.logger import logger


class DatabricksWriter:

    def __init__(self):

        self.client = WorkspaceClient()

        logger.info(
            "Connected to Databricks."
        )

    def sync_blob(self, blob):

        logger.info(
            f"Processing {blob.name}"
        )

        # TODO

        # 1. Check whether file exists

        # 2. Compare metadata

        # 3. Upload if changed

        return True