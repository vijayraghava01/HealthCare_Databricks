import random

import pandas as pd

from faker import Faker

from data_generator.common.data_loader import DataLoader
from data_generator.common.writer import CsvWriter
from data_generator.common.conifg_loader import ConfigLoader

from data_generator.common.constants import (
    ENCOUNTER_TYPES,
    ENCOUNTER_STATUS,
    ENCOUNTER_STATUS_WEIGHTS
)

fake = Faker("en_US")

Faker.seed(42)
random.seed(42)


class EncounterGenerator:

    def __init__(self):

        self.config = ConfigLoader.load()

    def generate(self):

        appointments = DataLoader.load_csv(
            "output/raw/appointments.csv"
        )

        encounters = []

        for i, appointment in enumerate(
            appointments.itertuples(index=False),
            start=1
        ):

            encounter_type = random.choice(
                ENCOUNTER_TYPES
            )

            status = random.choices(

                ENCOUNTER_STATUS,

                weights=ENCOUNTER_STATUS_WEIGHTS,

                k=1

            )[0]

            duration = random.randint(
                15,
                180
            )

            encounters.append({

                "Encounter_ID":
                    f"ENC{i:06}",

                "Appointment_ID":
                    appointment.Appointment_ID,

                "Patient_ID":
                    appointment.Patient_ID,

                "Provider_ID":
                    appointment.Provider_ID,

                "Hospital_ID":
                    appointment.Hospital_ID,

                "Diagnosis_ID":
                    appointment.Diagnosis_ID,

                "Encounter_Type":
                    encounter_type,

                "Encounter_Status":
                    status,

                "Duration_Minutes":
                    duration,

                "Encounter_Date":
                    appointment.Appointment_Date,

                "Created_Date":
                    appointment.Created_Date,

                "Updated_Date":
                    appointment.Updated_Date

            })

        df = pd.DataFrame(encounters)

        CsvWriter.write(

            df,

            "output/raw/encounters.csv"

        )

        print(
            f"Generated {len(df)} Encounters"
        )

        return df