from datetime import datetime, timedelta

import pandas as pd
import random
from faker import Faker

from data_generator.common.writer import CsvWriter
from data_generator.common.conifg_loader import ConfigLoader  # type: ignore


fake = Faker("en_US")

Faker.seed(42)
random.seed(42)


class PatientGenerator:
    def __init__(self):
        self.config = ConfigLoader.load()
        self.row_count = self.config["patients"]["rows"]

    def _generate_patient(self, patient_number):
        dob = fake.date_between(
            start_date="-95y",
            end_date="-1d",
        )

        created = fake.date_between(
            start_date="-5y",
            end_date="today",
        )

        return {
            "Patient_ID": f"P{patient_number:06}",
            "MRN": fake.unique.bothify(
                text="MRN######",
            ),
            "First_Name": fake.first_name(),
            "Last_Name": fake.last_name(),
            "DOB": dob,
            "Gender": random.choice(
                ["Male", "Female"],
            ),
            "Phone": fake.phone_number(),
            "Email": fake.email(),
            "Address": fake.street_address(),
            "City": fake.city(),
            "State": fake.state_abbr(),
            "Zip_Code": fake.postcode(),
            "Created_Date": created,
            "Updated_Date": created,
        }

    def _generate_patients(self, start_patient_number, row_count):
        return [
            self._generate_patient(patient_number)
            for patient_number in range(
                start_patient_number,
                start_patient_number + row_count,
            )
        ]

    def generate(self):
        patients = self._generate_patients(
            start_patient_number=1,
            row_count=self.row_count,
        )

        df = pd.DataFrame(patients)

        CsvWriter.write(
            df,
            "output/raw/patients.csv",
        )

        print(f"Generated {len(df)} Patients")

        return df

    def generate_incremental(
        self,
        start_patient_number,
        row_count=100,
        output_file="output/raw/patients_increment_001.csv",
    ):
        patients = self._generate_patients(
            start_patient_number=start_patient_number,
            row_count=row_count,
        )

        df = pd.DataFrame(patients)

        CsvWriter.write(
            df,
            output_file,
        )

        print(
            f"Generated {len(df)} incremental patients",
        )

        print(
            f"Patient IDs: "
            f"P{start_patient_number:06} "
            f"to "
            f"P{start_patient_number + row_count - 1:06}",
        )

        return df
    
    def generate_duplicate(
        self,
        start_patient_number,
        row_count=100,
        filepath="output/raw/patients_duplicate_002.csv"
    ):
        patients=self._generate_patients(
            start_patient_number,
            row_count
        )
        
        df=pd.DataFrame(patients)
        CsvWriter.write(
            df,
            file_path=filepath
        )
        print(f"Generated duplicate {len(df)} Patients")
        
        return df