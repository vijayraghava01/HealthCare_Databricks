import random

import pandas as pd

from faker import Faker

from data_generator.common.data_loader import DataLoader
from data_generator.common.writer import CsvWriter
from data_generator.common.conifg_loader import ConfigLoader

from data_generator.common.constants import (
    DISCHARGE_DISPOSITION,
    DISCHARGE_DISPOSITION_WEIGHTS
)

fake = Faker("en_US")

Faker.seed(42)
random.seed(42)


class DischargeGenerator:

    def __init__(self):

        self.config = ConfigLoader.load()

    def generate(self):

        admissions = DataLoader.load_csv(
            "output/raw/admissions.csv"
        )

        discharges = []

        for i, admission in enumerate(
            admissions.itertuples(index=False),
            start=1
        ):

            admission_date = pd.to_datetime(
                admission.Admission_Date
            )

            length_of_stay = random.randint(
                1,
                15
            )

            discharge_date = (
                admission_date +
                pd.Timedelta(
                    days=length_of_stay
                )
            )

            disposition = random.choices(

                DISCHARGE_DISPOSITION,

                weights=DISCHARGE_DISPOSITION_WEIGHTS,

                k=1

            )[0]

            readmission = random.choice(
                [
                    "Yes",
                    "No"
                ]
            )

            discharges.append({

                "Discharge_ID":
                    f"DIS{i:06}",

                "Admission_ID":
                    admission.Admission_ID,

                "Encounter_ID":
                    admission.Encounter_ID,

                "Patient_ID":
                    admission.Patient_ID,

                "Hospital_ID":
                    admission.Hospital_ID,

                "Discharge_Date":
                    discharge_date,

                "Length_of_Stay":
                    length_of_stay,

                "Discharge_Disposition":
                    disposition,

                "Readmission_Flag":
                    readmission,

                "Created_Date":
                    admission.Created_Date,

                "Updated_Date":
                    admission.Updated_Date

            })

        df = pd.DataFrame(
            discharges
        )

        CsvWriter.write(

            df,

            "output/raw/discharges.csv"

        )

        print(
            f"Generated {len(df)} Discharges"
        )

        return df