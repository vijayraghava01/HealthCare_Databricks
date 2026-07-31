import random

import pandas as pd

from faker import Faker

from data_generator.common.writer import CsvWriter
from data_generator.common.constants import (
    AUDIT_ACTIONS,
    ENTITY_TYPES,
    USERS
)

fake = Faker("en_US")

Faker.seed(42)
random.seed(42)


class AuditGenerator:

    def generate(self):

        audit_logs = []

        for i in range(1, 50001):

            audit_logs.append({

                "Audit_ID":
                    f"AUD{i:06}",

                "Entity_Type":
                    random.choice(
                        ENTITY_TYPES
                    ),

                "Entity_ID":
                    fake.uuid4(),

                "Action":
                    random.choice(
                        AUDIT_ACTIONS
                    ),

                "Changed_By":
                    random.choice(
                        USERS
                    ),

                "Event_Timestamp":
                    fake.date_time_between(
                        "-2y",
                        "now"
                    )

            })

        df = pd.DataFrame(
            audit_logs
        )

        CsvWriter.write(
            df,
            "output/raw/audit_logs.csv"
        )

        print(
            f"Generated {len(df)} Audit Logs"
        )

        return df