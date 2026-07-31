import random

from datetime import datetime
from datetime import timedelta

import pandas as pd

from faker import Faker

from data_generator.common.data_loader import DataLoader
from data_generator.common.writer import CsvWriter
from data_generator.common.conifg_loader import ConfigLoader

from data_generator.common.constants import (
    VISIT_TYPES,
    VISIT_TYPE_WEIGHTS,
    APPOINTMENT_STATUS,
    APPOINTMENT_STATUS_WEIGHTS,
    PRIORITY,
    PRIORITY_WEIGHTS,
    BUSINESS_START_HOUR,
    BUSINESS_END_HOUR
)

fake = Faker()

Faker.seed(42)
random.seed(42)


class AppointmentGenerator:

    def __init__(self):

        config = ConfigLoader.load()

        self.rows = config["appointments"]["rows"]

    def generate(self):

        patients = DataLoader.load_csv(
            "output/raw/patients.csv"
        )

        providers = DataLoader.load_csv(
            "output/raw/providers.csv"
        )

        diagnosis = DataLoader.load_csv(
            "output/raw/diagnosis_codes.csv"
        )

        appointments = []

        for i in range(1, self.rows + 1):

            patient = patients.sample(1).iloc[0]

            provider = providers.sample(1).iloc[0]

            eligible = diagnosis[
                diagnosis["Specialty"] ==
                provider["Specialty"]
            ]

            if eligible.empty:

                eligible = diagnosis

            diagnosis_row = eligible.sample(1).iloc[0]

            visit_type = random.choices(
                VISIT_TYPES,
                weights=VISIT_TYPE_WEIGHTS,
                k=1
            )[0]

            appointment_status = random.choices(
                APPOINTMENT_STATUS,
                weights=APPOINTMENT_STATUS_WEIGHTS,
                k=1
            )[0]

            priority = random.choices(
                PRIORITY,
                weights=PRIORITY_WEIGHTS,
                k=1
            )[0]

            appointment_date = fake.date_between(
                "-3y",
                "today"
            )

            hour = random.randint(
                BUSINESS_START_HOUR,
                BUSINESS_END_HOUR - 1
            )

            minute = random.choice(
                [0, 15, 30, 45]
            )

            start_datetime = datetime(
                appointment_date.year,
                appointment_date.month,
                appointment_date.day,
                hour,
                minute
            )

            if visit_type == "Outpatient":

                duration = random.randint(15, 45)

            elif visit_type == "Emergency":

                duration = random.randint(30, 180)

            else:

                duration = random.randint(60, 240)

            end_datetime = (
                start_datetime +
                timedelta(minutes=duration)
            )

            appointments.append({

                "Appointment_ID":
                    f"APT{i:06}",

                "Patient_ID":
                    patient["Patient_ID"],

                "Provider_ID":
                    provider["Provider_ID"],

                "Hospital_ID":
                    provider["Hospital_ID"],

                "Hospital_Name":
                    provider["Hospital_Name"],

                "Department":
                    provider["Specialty"],

                "Diagnosis_ID":
                    diagnosis_row["Diagnosis_ID"],

                "Visit_Type":
                    visit_type,

                "Appointment_Status":
                    appointment_status,

                "Priority":
                    priority,

                "Appointment_Date":
                    appointment_date,

                "Start_Time":
                    start_datetime.strftime("%H:%M"),

                "End_Time":
                    end_datetime.strftime("%H:%M"),

                "Duration_Minutes":
                    duration,

                "Created_Date":
                    appointment_date,

                "Updated_Date":
                    appointment_date

            })

        df = pd.DataFrame(appointments)

        CsvWriter.write(
            df,
            "output/raw/appointments.csv"
        )

        print(df.head())

        return df