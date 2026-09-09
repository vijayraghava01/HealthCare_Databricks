from ingestion_service.azure_reader import AzureReader
from ingestion_service.databricks_uploader import DatabricksWriter
from ingestion_service.logger import logger


class SyncManager:

    def __init__(self):

        self.azure = AzureReader()

        self.writer = DatabricksWriter()

    def synchronize(self):

        files = self.azure.list_files()

        logger.info(
            f"Starting synchronization of {len(files)} files."
        )

        uploaded = 0

        skipped = 0

        for blob in files:

            if self.writer.sync_blob(blob):

                uploaded += 1

            else:

                skipped += 1

        logger.info(
            f"Synchronization Complete."
        )

        logger.info(
            f"Uploaded : {uploaded}"
        )

        logger.info(
            f"Skipped  : {skipped}"
        )