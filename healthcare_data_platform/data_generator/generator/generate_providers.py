import random

import pandas as pd

from faker import Faker

from data_generator.common.data_loader   import DataLoader
from data_generator.common.constants import SPECIALTIES
from data_generator.common.writer import CsvWriter
from data_generator.common.conifg_loader import ConfigLoader

fake = Faker()

Faker.seed(42)
random.seed(42)


class ProviderGenerator:

    def __init__(self):

        config = ConfigLoader.load()

        self.rows = config["providers"]["rows"]

    def generate(self):

        hospitals = DataLoader.load_csv(
            "output/raw/hospitals.csv"
        )

        providers = []

        for i in range(1, self.rows + 1):

            hospital = hospitals.sample(1).iloc[0]

            providers.append({

                "Provider_ID": f"PR{i:06}",

                "NPI": random.randint(
                    1000000000,
                    9999999999
                ),

                "First_Name": fake.first_name(),

                "Last_Name": fake.last_name(),

                "Specialty": random.choice(
                    SPECIALTIES
                ),

                "Hospital_ID":
                    hospital["Hospital_ID"],

                "Hospital_Name":
                    hospital["Hospital_Name"],

                "State":
                    hospital["State"],

                "Years_Experience":
                    random.randint(1,40),

                "Status":
                    "Active",

                "Created_Date":
                    fake.date_between("-10y","-2y"),

                "Updated_Date":
                    fake.date_between("-2y","today")

            })

        df = pd.DataFrame(providers)

        CsvWriter.write(
            df,
            "output/raw/providers.csv"
        )

        print(df.head())

        return df