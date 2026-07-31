import os

from data_generator.common.azure_uploader import AzureUploader


class CsvWriter:

    @staticmethod
    def write(

        df,

        file_path

    ):

        os.makedirs(

            os.path.dirname(file_path),

            exist_ok=True

        )

        df.to_csv(

            file_path,

            index=False

        )

        print(

            f"Saved -> {file_path}"

        )

        file_name = os.path.basename(file_path)

        dataset_name = os.path.splitext(file_name)[0]

        remote_path = f"{dataset_name}/{file_name}"

        AzureUploader.upload(

            file_path,

            remote_path

        )