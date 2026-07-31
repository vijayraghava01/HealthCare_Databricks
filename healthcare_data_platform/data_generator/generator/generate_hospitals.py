import random
import pandas as pd

from faker import Faker

from data_generator.common.writer import CsvWriter
from data_generator.common.conifg_loader import ConfigLoader
from data_generator.common.constants import (
    HOSPITAL_TYPES,
    REGIONS,
    TRAUMA_LEVEL
)

fake = Faker("en_US")

Faker.seed(42)
random.seed(42)


class HospitalGenerator:

    def __init__(self):

        config = ConfigLoader.load()

        self.rows = config["hospitals"]["rows"]

    def generate(self):

        hospitals = []

        for i in range(1, self.rows + 1):

            hospitals.append({

                "Hospital_ID": f"H{i:04}",

                "Hospital_Name":
                    fake.company() + " Hospital",

                "Hospital_Type":
                    random.choice(HOSPITAL_TYPES),

                "Region":
                    random.choice(REGIONS),

                "City":
                    fake.city(),

                "State":
                    fake.state_abbr(),

                "Bed_Count":
                    random.randint(50,1000),

                "Trauma_Level":
                    random.choice(TRAUMA_LEVEL),

                "Teaching_Hospital":
                    random.choice([True,False]),

                "Active":
                    random.choice([True,True,True,False]),

                "Created_Date":
                    fake.date_between("-10y","-2y")

            })

        df = pd.DataFrame(hospitals)

        CsvWriter.write(
            df,
            "output/raw/hospitals.csv"
        )

        print(f"{len(df)} Hospitals Generated")

        return df