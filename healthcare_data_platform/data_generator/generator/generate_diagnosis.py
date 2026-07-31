import random
import pandas as pd
from faker import Faker

from data_generator.common.writer import CsvWriter
from data_generator.common.conifg_loader import ConfigLoader
from data_generator.common.constants import DIAGNOSIS_MASTER

fake = Faker()


class DiagnosisGenerator:

    def __init__(self):

        config = ConfigLoader.load()

        self.rows = config["diagnosis"]["rows"]

    def generate(self):

        rows = []

        for i in range(self.rows):

            code, diagnosis, specialty = random.choice(DIAGNOSIS_MASTER)

            rows.append({

                "Diagnosis_ID":f"DX{i+1:06}",

                "ICD10_Code":code,

                "Diagnosis_Name":diagnosis,

                "Specialty":specialty,

                "Severity":random.choice([
                    "Low",
                    "Medium",
                    "High",
                    "Critical"
                ]),

                "Chronic_Flag":random.choice([
                    "Yes",
                    "No"
                ]),

                "Active":"Yes",

                "Created_Date":
                    fake.date_between("-5y","today")

            })

        df = pd.DataFrame(rows)

        CsvWriter.write(
            df,
            "output/raw/diagnosis_codes.csv"
        )

        print(df.head())

        return df