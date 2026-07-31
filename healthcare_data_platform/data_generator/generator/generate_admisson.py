import random

import pandas as pd

from faker import Faker

from data_generator.common.data_loader import DataLoader
from data_generator.common.writer import CsvWriter
from data_generator.common.conifg_loader import ConfigLoader

from data_generator.common.constants import (
    ADMISSION_TYPES,
    ADMISSION_STATUS,
    ADMISSION_STATUS_WEIGHTS,
    ROOM_TYPES
)

fake = Faker("en_US")

Faker.seed(42)
random.seed(42)


class AdmissionGenerator:

    def __init__(self):

        self.config = ConfigLoader.load()

    def generate(self):

        encounters = DataLoader.load_csv(
            "output/raw/encounters.csv"
        )

        admissions = []

        admission_number = 1

        for _, encounter in encounters.iterrows():

            # Approximately 20% of encounters become admissions
            if random.random() > 0.20:
                continue

            admission_date = pd.to_datetime(
                encounter["Encounter_Date"]
            )

            admissions.append({

                "Admission_ID":
                    f"ADM{admission_number:06}",

                "Encounter_ID":
                    encounter["Encounter_ID"],

                "Patient_ID":
                    encounter["Patient_ID"],

                "Hospital_ID":
                    encounter["Hospital_ID"],

                "Admission_Type":
                    random.choice(
                        ADMISSION_TYPES
                    ),

                "Admission_Status":
                    random.choices(

                        ADMISSION_STATUS,

                        weights=ADMISSION_STATUS_WEIGHTS,

                        k=1

                    )[0],

                "Ward":
                    random.choice(
                        ROOM_TYPES
                    ),

                "Room_Number":
                    random.randint(
                        100,
                        999
                    ),

                "Bed_Number":
                    random.randint(
                        1,
                        6
                    ),

                "Admission_Date":
                    admission_date,

                "Created_Date":
                    encounter["Created_Date"],

                "Updated_Date":
                    encounter["Updated_Date"]

            })

            admission_number += 1

        df = pd.DataFrame(admissions)

        CsvWriter.write(

            df,

            "output/raw/admissions.csv"

        )

        print(
            f"Generated {len(df)} Admissions"
        )

        return df