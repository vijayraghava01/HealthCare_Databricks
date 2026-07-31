import random

import pandas as pd

from faker import Faker

from data_generator.common.data_loader import DataLoader
from data_generator.common.writer import CsvWriter
from data_generator.common.conifg_loader import ConfigLoader

from data_generator.common.constants import (
    LAB_TESTS,
    RESULT_STATUS,
    RESULT_STATUS_WEIGHTS
)

fake = Faker("en_US")

Faker.seed(42)
random.seed(42)


class LabResultGenerator:

    def __init__(self):

        self.config = ConfigLoader.load()

    def generate(self):

        appointments = DataLoader.load_csv(
            "output/raw/appointments.csv"
        )

        lab_results = []

        for i, appointment in enumerate(
            appointments.itertuples(index=False),
            start=1
        ):

            test = random.choice(
                LAB_TESTS
            )

            status = random.choices(

                RESULT_STATUS,

                weights=RESULT_STATUS_WEIGHTS,

                k=1

            )[0]

            if status == "Normal":

                result = round(

                    random.uniform(
                        test["Min"],
                        test["Max"]
                    ),

                    2

                )

            elif status == "High":

                result = round(

                    random.uniform(
                        test["Max"] + 1,
                        test["Max"] + 20
                    ),

                    2

                )

            elif status == "Low":

                result = round(

                    random.uniform(
                        max(0, test["Min"] - 20),
                        test["Min"] - 1
                    ),

                    2

                )

            else:

                result = round(

                    random.uniform(
                        test["Max"] + 20,
                        test["Max"] + 80
                    ),

                    2

                )

            lab_results.append({

                "Lab_Result_ID":
                    f"LAB{i:06}",

                "Appointment_ID":
                    appointment.Appointment_ID,

                "Patient_ID":
                    appointment.Patient_ID,

                "Provider_ID":
                    appointment.Provider_ID,

                "Test_Name":
                    test["Test_Name"],

                "Result_Value":
                    result,

                "Unit":
                    test["Unit"],

                "Reference_Range":
                    f'{test["Min"]}-{test["Max"]}',

                "Result_Status":
                    status,

                "Result_Date":
                    appointment.Appointment_Date,

                "Created_Date":
                    appointment.Created_Date,

                "Updated_Date":
                    appointment.Updated_Date

            })

        df = pd.DataFrame(
            lab_results
        )

        CsvWriter.write(

            df,

            "output/raw/lab_results.csv"

        )

        print(
            f"Generated {len(df)} Lab Results"
        )

        return df