from abc import ABC, abstractmethod


class BaseGenerator(ABC):

    def __init__(self, config):
        self.config = config

    @abstractmethod
    def generate(self):
        pass

    def validate(self, dataframe):
        """
        Override in child classes if needed.
        """
        return dataframe

    def save(self, dataframe, writer, output_path):
        writer.write(dataframe, output_path)