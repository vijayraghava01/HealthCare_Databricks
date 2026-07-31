import random

import pandas as pd

from faker import Faker

from data_generator.common.data_loader import DataLoader
from data_generator.common.writer import CsvWriter
from data_generator.common.conifg_loader import ConfigLoader

from data_generator.common.constants import (
    PRESCRIPTION_STATUS,
    PRESCRIPTION_STATUS_WEIGHTS,
    DOSAGE_FREQUENCY,
    DURATION_DAYS
)

fake = Faker("en_US")

Faker.seed(42)
random.seed(42)


class PrescriptionGenerator:

    def __init__(self):

        self.config = ConfigLoader.load()

    def generate(self):

        appointments = DataLoader.load_csv(
            "output/raw/appointments.csv"
        )

        medications = DataLoader.load_csv(
            "output/raw/medications.csv"
        )

        prescriptions = []

        for i, appointment in enumerate(
            appointments.itertuples(index=False),
            start=1
        ):

            medication = medications.sample(1).iloc[0]

            status = random.choices(

                PRESCRIPTION_STATUS,

                weights=PRESCRIPTION_STATUS_WEIGHTS,

                k=1

            )[0]

            duration = random.choice(
                DURATION_DAYS
            )

            prescriptions.append({

                "Prescription_ID":
                    f"RX{i:06}",

                "Appointment_ID":
                    appointment.Appointment_ID,

                "Patient_ID":
                    appointment.Patient_ID,

                "Provider_ID":
                    appointment.Provider_ID,

                "Medication_ID":
                    medication["Medication_ID"],

                "Medication_Name":
                    medication["Brand_Name"],

                "Strength":
                    medication["Strength"],

                "Dosage":
                    random.choice(
                        DOSAGE_FREQUENCY
                    ),

                "Duration_Days":
                    duration,

                "Quantity":
                    duration,

                "Status":
                    status,

                "Prescription_Date":
                    appointment.Appointment_Date,

                "Created_Date":
                    appointment.Created_Date,

                "Updated_Date":
                    appointment.Updated_Date

            })

        df = pd.DataFrame(
            prescriptions
        )

        CsvWriter.write(

            df,

            "output/raw/prescriptions.csv"

        )

        print(
            f"Generated {len(df)} Prescriptions"
        )

        return df