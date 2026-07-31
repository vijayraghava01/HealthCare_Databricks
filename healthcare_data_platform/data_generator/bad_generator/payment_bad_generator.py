import pandas as pd

from data_generator.common.data_loader import DataLoader
from data_generator.common.writer import CsvWriter


class PaymentBadGenerator:

    def generate(self):

        payments = DataLoader.load_csv(
            "output/raw/payments.csv"
        )

        bad = payments.sample(
            frac=0.02,
            random_state=42
        ).copy().reset_index(drop=True)

        # Duplicate Payment_ID
        bad.loc[0, "Payment_ID"] = (
            payments.iloc[1]["Payment_ID"]
        )

        # Invalid Claim_ID
        bad.loc[1, "Claim_ID"] = "CLM999999"

        # Invalid Patient_ID
        bad.loc[2, "Patient_ID"] = "P999999"

        # Negative Payment Amount
        bad.loc[3, "Payment_Amount"] = -500

        # Extremely Large Payment
        bad.loc[4, "Payment_Amount"] = 9999999

        # Invalid Payment Method
        bad.loc[5, "Payment_Method"] = "Crypto"

        # Invalid Payment Status
        bad.loc[6, "Payment_Status"] = "PROCESSING"

        # Null Payment Method
        bad.loc[7, "Payment_Method"] = None

        # Future Payment Date
        bad.loc[8, "Payment_Date"] = "2055-01-01"

        # Null Claim_ID
        bad.loc[9, "Claim_ID"] = None

        CsvWriter.write(

            bad,

            "output/bad_data/payments_bad.csv"

        )

        print(

            f"Generated {len(bad)} Bad Payments"

        )

        return bad