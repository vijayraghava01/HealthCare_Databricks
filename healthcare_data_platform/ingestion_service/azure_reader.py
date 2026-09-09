
from azure.storage.blob import BlobServiceClient

from ingestion_service.config import (
    AZURE_STORAGE_CONNECTION_STRING,
    CONTAINER_NAME
)

from ingestion_service.logger import logger


class AzureReader:

    def __init__(self):

        self.client = BlobServiceClient.from_connection_string(
            AZURE_STORAGE_CONNECTION_STRING
        )

        self.container = self.client.get_container_client(
            CONTAINER_NAME
        )

        logger.info(
            "Connected to Azure Blob Storage."
        )
      

    def list_files(self):

        files = []

        for blob in self.container.list_blobs():

            if "." in blob.name:

                files.append(blob)

        logger.info(
            f"{len(files)} files discovered."
        )

        return files