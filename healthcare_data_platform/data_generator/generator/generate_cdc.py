import random

import pandas as pd

from faker import Faker

from data_generator.common.data_loader import DataLoader
from data_generator.common.writer import CsvWriter

from data_generator.common.constants import CDC_OPERATIONS

fake = Faker("en_US")

Faker.seed(42)
random.seed(42)


class CDCGenerator:

    def generate(self):

        patients = DataLoader.load_csv(
            "output/raw/patients.csv"
        )

        cdc_events = []

        for i, patient in enumerate(
            patients.itertuples(index=False),
            start=1
        ):

            cdc_events.append({

                "CDC_Event_ID":
                    f"CDC{i:06}",

                "Entity":
                    "Patient",

                "Entity_ID":
                    patient.Patient_ID,

                "Operation":
                    random.choice(
                        CDC_OPERATIONS
                    ),

                "Event_Time":
                    fake.date_time_between(
                        "-1y",
                        "now"
                    )

            })

        df = pd.DataFrame(
            cdc_events
        )

        CsvWriter.write(
            df,
            "output/raw/cdc_events.csv"
        )

        print(
            f"Generated {len(df)} CDC Events"
        )

        return df