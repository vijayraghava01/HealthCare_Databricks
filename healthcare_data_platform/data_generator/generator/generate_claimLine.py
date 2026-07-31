import random

import pandas as pd

from faker import Faker

from data_generator.common.data_loader import DataLoader
from data_generator.common.writer import CsvWriter
from data_generator.common.conifg_loader import ConfigLoader

from data_generator.common.constants import (
    LINE_STATUS,
    LINE_STATUS_WEIGHTS,
    MIN_LINE_ITEMS,
    MAX_LINE_ITEMS
)

fake = Faker("en_US")

Faker.seed(42)
random.seed(42)


class ClaimLineGenerator:

    def __init__(self):

        self.config = ConfigLoader.load()

    def generate(self):

        claims = DataLoader.load_csv(
            "output/raw/claims.csv"
        )

        procedures = DataLoader.load_csv(
            "output/raw/procedures.csv"
        )

        claim_lines = []

        line_id = 1

        for _, claim in claims.iterrows():

            number_of_lines = random.randint(
                MIN_LINE_ITEMS,
                MAX_LINE_ITEMS
            )

            for line_number in range(
                1,
                number_of_lines + 1
            ):

                procedure = procedures.sample(
                    1
                ).iloc[0]

                units = random.randint(
                    1,
                    3
                )

                unit_cost = float(
                    procedure["Procedure_Cost"]
                )

                charge = round(
                    units * unit_cost,
                    2
                )

                coverage = claim[
                    "Coverage_Percentage"
                ]

                allowed = charge

                insurance_payment = round(
                    (
                        allowed *
                        coverage
                    ) / 100,
                    2
                )

                patient_responsibility = round(
                    allowed -
                    insurance_payment,
                    2
                )

                status = random.choices(

                    LINE_STATUS,

                    weights=LINE_STATUS_WEIGHTS,

                    k=1

                )[0]

                claim_lines.append({

                    "Claim_Line_ID":
                        f"CLN{line_id:08}",

                    "Claim_ID":
                        claim["Claim_ID"],

                    "Line_Number":
                        line_number,

                    "Procedure_ID":
                        procedure["Procedure_ID"],

                    "CPT_Code":
                        procedure["CPT_Code"],

                    "Procedure_Name":
                        procedure["Procedure_Name"],

                    "Units":
                        units,

                    "Unit_Cost":
                        unit_cost,

                    "Charge_Amount":
                        charge,

                    "Allowed_Amount":
                        allowed,

                    "Insurance_Payment":
                        insurance_payment,

                    "Patient_Responsibility":
                        patient_responsibility,

                    "Line_Status":
                        status,

                    "Created_Date":
                        claim["Created_Date"],

                    "Updated_Date":
                        claim["Updated_Date"]

                })

                line_id += 1

        df = pd.DataFrame(
            claim_lines
        )

        CsvWriter.write(

            df,

            "output/raw/claim_lines.csv"

        )

        print(
            f"Generated {len(df)} Claim Lines"
        )

        return df