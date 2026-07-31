from faker import Faker
import pandas as pd
import random
from datetime import datetime, timedelta

from data_generator.common.writer import CsvWriter
from data_generator.common.conifg_loader import ConfigLoader #type:ignore

fake = Faker("en_US")

Faker.seed(42)
random.seed(42)


class PatientGenerator:

    def __init__(self):

        self.config = ConfigLoader.load()

        self.row_count = self.config["patients"]["rows"]

    def generate(self):

        patients = []

        for i in range(1, self.row_count + 1):

            dob = fake.date_between(
                start_date="-95y",
                end_date="-1d"
            )

            created = fake.date_between(
                start_date="-5y",
                end_date="today"
            )

            patient = {

                "Patient_ID": f"P{i:06}",

                "MRN": fake.unique.bothify(
                    text="MRN######"
                ),

                "First_Name": fake.first_name(),

                "Last_Name": fake.last_name(),

                "DOB": dob,

                "Gender": random.choice(
                    ["Male", "Female"]
                ),

                "Phone": fake.phone_number(),

                "Email": fake.email(),

                "Address": fake.street_address(),

                "City": fake.city(),

                "State": fake.state_abbr(),

                "Zip_Code": fake.postcode(),

                "Created_Date": created,

                "Updated_Date": created

            }

            patients.append(patient)

        df = pd.DataFrame(patients)

        CsvWriter.write(
            df,
            "output/raw/patients.csv"
        )

        print(
            f"Generated {len(df)} Patients"
        )

        return df