from pathlib import Path


class OutputManager:

    @staticmethod
    def raw_file(name: str) -> str:
        path = Path("output/raw")
        path.mkdir(parents=True, exist_ok=True)
        return str(path / f"{name}.csv")

    @staticmethod
    def bad_file(name: str) -> str:
        path = Path("output/bad_data")
        path.mkdir(parents=True, exist_ok=True)
        return str(path / f"{name}.csv")

    @staticmethod
    def streaming_folder() -> str:
        path = Path("output/streaming")
        path.mkdir(parents=True, exist_ok=True)
        return str(path)

    @staticmethod
    def cdc_folder() -> str:
        path = Path("output/cdc")
        path.mkdir(parents=True, exist_ok=True)
        return str(path)