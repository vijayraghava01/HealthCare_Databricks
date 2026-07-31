import pandas as pd

from data_generator.common.data_loader import DataLoader
from data_generator.common.writer import CsvWriter


class ClaimBadGenerator:

    def generate(self):

        claims = DataLoader.load_csv(
            "output/raw/claims.csv"
        )

        bad = claims.sample(
            frac=0.02,
            random_state=42
        ).copy().reset_index(drop=True)

        # Duplicate Claim_ID
        bad.loc[0, "Claim_ID"] = claims.iloc[1]["Claim_ID"]

        # Invalid Patient_ID
        bad.loc[1, "Patient_ID"] = "P999999"

        # Invalid Procedure_ID
        bad.loc[2, "Procedure_ID"] = "PROC999999"

        # Negative Charge
        bad.loc[3, "Charge_Amount"] = -500

        # Insurance Payment > Charge
        bad.loc[4, "Insurance_Payment"] = (
            bad.loc[4, "Charge_Amount"] + 1000
        )

        # Coverage > 100%
        bad.loc[5, "Coverage_Percentage"] = 150

        # Negative Patient Responsibility
        bad.loc[6, "Patient_Responsibility"] = -250

        # Invalid Claim Status
        bad.loc[7, "Claim_Status"] = "PROCESSING"

        # Null Insurance Plan
        bad.loc[8, "Plan_Name"] = None

        # Future Claim Date
        bad.loc[9, "Claim_Date"] = "2055-01-01"

        # Null Procedure_ID
        bad.loc[10, "Procedure_ID"] = None

        # Negative Allowed Amount
        bad.loc[11, "Allowed_Amount"] = -100

        CsvWriter.write(

            bad,

            "output/bad_data/claims_bad.csv"

        )

        print(

            f"Generated {len(bad)} Bad Claims"

        )

        return bad