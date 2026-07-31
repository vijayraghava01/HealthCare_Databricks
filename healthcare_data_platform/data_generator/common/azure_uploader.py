import os

from azure.identity import DefaultAzureCredential
from azure.storage.filedatalake import DataLakeServiceClient

from data_generator.common.azure_config import AzureConfig


class AzureUploader:

    credential = DefaultAzureCredential()

    service_client = DataLakeServiceClient(

        account_url=AzureConfig.ACCOUNT_URL,

        credential=credential

    )

    file_system = service_client.get_file_system_client(

        AzureConfig.FILE_SYSTEM

    )

    @classmethod
    def upload(

        cls,

        local_path,

        remote_path

    ):

        directory = os.path.dirname(

            remote_path

        )

        if directory:

            try:

                cls.file_system.create_directory(

                    directory

                )

            except:

                pass

        file_client = cls.file_system.get_file_client(

            remote_path

        )

        with open(

            local_path,

            "rb"

        ) as file:

            file_client.upload_data(

                file,

                overwrite=True

            )

        print(

            f"Uploaded -> {remote_path}"

        )