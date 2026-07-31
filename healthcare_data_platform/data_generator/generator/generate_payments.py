import random

import pandas as pd

from faker import Faker

from data_generator.common.data_loader import DataLoader
from data_generator.common.writer import CsvWriter
from data_generator.common.conifg_loader import ConfigLoader

from data_generator.common.constants import (
    PAYMENT_METHODS,
    PAYMENT_STATUS,
    PAYMENT_STATUS_WEIGHTS
)

fake = Faker("en_US")

Faker.seed(42)
random.seed(42)


class PaymentGenerator:

    def __init__(self):

        self.config = ConfigLoader.load()

    def generate(self):

        claims = DataLoader.load_csv(
            "output/raw/claims.csv"
        )

        payments = []

        for i, claim in enumerate(
            claims.itertuples(index=False),
            start=1
        ):

            status = random.choices(

                PAYMENT_STATUS,

                weights=PAYMENT_STATUS_WEIGHTS,

                k=1

            )[0]

            payment_amount = claim.Insurance_Payment

            if status == "Partial Paid":

                payment_amount = round(

                    payment_amount * 0.50,

                    2

                )

            elif status == "Pending":

                payment_amount = 0

            elif status == "Failed":

                payment_amount = 0

            payment = {

                "Payment_ID":
                    f"PAY{i:06}",

                "Claim_ID":
                    claim.Claim_ID,

                "Patient_ID":
                    claim.Patient_ID,

                "Payment_Method":
                    random.choice(
                        PAYMENT_METHODS
                    ),

                "Payment_Status":
                    status,

                "Payment_Amount":
                    payment_amount,

                "Payment_Date":
                    fake.date_between(
                        "-2y",
                        "today"
                    ),

                "Created_Date":
                    claim.Created_Date,

                "Updated_Date":
                    claim.Updated_Date

            }

            payments.append(payment)

        df = pd.DataFrame(payments)

        CsvWriter.write(

            df,

            "output/raw/payments.csv"

        )

        print(

            f"Generated {len(df)} Payments"

        )

        return df