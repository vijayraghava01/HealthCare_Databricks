import random

import pandas as pd

from faker import Faker

from data_generator.common.data_loader import DataLoader
from data_generator.common.writer import CsvWriter
from data_generator.common.conifg_loader import ConfigLoader

from data_generator.common.constants import (
    CLAIM_STATUS,
    CLAIM_STATUS_WEIGHTS,
    COVERAGE_PERCENTAGES,
    DENIAL_REASONS
)

fake = Faker("en_US")

Faker.seed(42)
random.seed(42)


class ClaimGenerator:

    def __init__(self):

        self.config = ConfigLoader.load()

        self.row_count = self.config["claims"]["rows"]

    def generate(self):

        appointments = DataLoader.load_csv(
            "output/raw/appointments.csv"
        )

        patients = DataLoader.load_csv(
            "output/raw/patients.csv"
        )

        procedures = DataLoader.load_csv(
            "output/raw/procedures.csv"
        )

        insurance = DataLoader.load_csv(
            "output/raw/insurance_plans.csv"
        )

        claims = []

        total_rows = min(
            self.row_count,
            len(appointments)
        )

        for i in range(1, total_rows + 1):

            appointment = appointments.iloc[i - 1]

            patient = patients[
                patients["Patient_ID"]
                ==
                appointment["Patient_ID"]
            ].iloc[0]

            procedure = procedures.sample(
                1
            ).iloc[0]

            insurance_plan = insurance.sample(
                1
            ).iloc[0]

            charge_amount = float(
                procedure["Procedure_Cost"]
            )

            coverage_percentage = random.choice(
                COVERAGE_PERCENTAGES
            )

            allowed_amount = charge_amount

            insurance_payment = round(
                (
                    allowed_amount
                    *
                    coverage_percentage
                ) / 100,
                2
            )

            patient_responsibility = round(
                allowed_amount -
                insurance_payment,
                2
            )

            claim_status = random.choices(

                CLAIM_STATUS,

                weights=CLAIM_STATUS_WEIGHTS,

                k=1

            )[0]

            denial_reason = ""

            if claim_status == "Denied":

                denial_reason = random.choice(
                    DENIAL_REASONS
                )

            claim = {

                "Claim_ID":
                    f"CLM{i:06}",

                "Appointment_ID":
                    appointment["Appointment_ID"],

                "Patient_ID":
                    patient["Patient_ID"],

                "Provider_ID":
                    appointment["Provider_ID"],

                "Hospital_ID":
                    appointment["Hospital_ID"],

                "Insurance_Plan":
                    insurance_plan["Plan_Name"],

                "Diagnosis_ID":
                    appointment["Diagnosis_ID"],

                "Procedure_ID":
                    procedure["Procedure_ID"],

                "CPT_Code":
                    procedure["CPT_Code"],

                "Procedure_Name":
                    procedure["Procedure_Name"],

                "Procedure_Specialty":
                    procedure["Specialty"],

                "Charge_Amount":
                    charge_amount,

                "Allowed_Amount":
                    allowed_amount,

                "Coverage_Percentage":
                    coverage_percentage,

                "Insurance_Payment":
                    insurance_payment,

                "Patient_Responsibility":
                    patient_responsibility,

                "Claim_Status":
                    claim_status,

                "Denial_Reason":
                    denial_reason,

                "Claim_Date":
                    appointment["Appointment_Date"],

                "Created_Date":
                    appointment["Created_Date"],

                "Updated_Date":
                    appointment["Updated_Date"]

            }

            claims.append(claim)

        df = pd.DataFrame(claims)

        CsvWriter.write(
            df,
            "output/raw/claims.csv"
        )

        print(
            f"Generated {len(df)} Claims"
        )

        return df