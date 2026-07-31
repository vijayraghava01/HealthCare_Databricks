from pathlib import Path
import yaml #type:ignore


class ConfigLoader:

    @staticmethod
    def load():

        config_path = (
            Path(__file__)
            .parent.parent
            / "config"
            / "generator.yml"
        )

        with open(config_path, "r") as file:
            return yaml.safe_load(file)