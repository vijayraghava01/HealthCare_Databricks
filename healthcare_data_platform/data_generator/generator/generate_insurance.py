import random
import pandas as pd
from faker import Faker
from data_generator.common.writer import CsvWriter
from data_generator.common.conifg_loader import ConfigLoader
fake =Faker()
from data_generator.common.constants import(
    STATE_CODES,
    NETWORK_TYPES,
    PLAN_COMPANIES,
    PLAN_TYPES
)


class InsuranceGenerator:

    def __init__(self):

        config = ConfigLoader.load()

        self.rows = config["insurance"]["rows"]

    def coverage(self, plan_type):

        if plan_type == "Medicare":
            return 80

        if plan_type == "Medicaid":
            return 95

        if plan_type == "Commercial":
            return random.randint(70,90)

        if plan_type == "PPO":
            return random.randint(85,90)

        if plan_type == "HMO":
            return random.randint(80,85)

        if plan_type == "EPO":
            return random.randint(75,85)

        return random.randint(80,90)

    def generate(self):

        rows = []

        for i in range(1,self.rows+1):

            company = random.choice(PLAN_COMPANIES)

            plan_type = random.choice(PLAN_TYPES)

            coverage = self.coverage(plan_type)

            rows.append({

                "Insurance_ID":f"INS{i:06}",

                "Plan_Name":
                    f"{company} {plan_type}",

                "Company":company,

                "Plan_Type":plan_type,

                "Coverage_Percentage":coverage,

                "Deductible":
                    random.choice(
                        [0,250,500,1000,1500,2000]
                    ),

                "CoPay":
                    random.choice(
                        [20,30,40,50,75]
                    ),

                "Out_of_Pocket_Max":
                    random.choice(
                        [2000,3000,4000,5000,7000]
                    ),

                "Network_Type":
                    random.choice(
                        NETWORK_TYPES
                    ),

                "State":
                    random.choice(
                        STATE_CODES
                    ),

                "Status":"Active",

                "Effective_Date":
                    fake.date_between("-5y","today"),

                "Expiry_Date":
                    fake.date_between("+1y","+5y")
            })

        df = pd.DataFrame(rows)

        CsvWriter.write(
            df,
            "output/raw/insurance_plans.csv"
        )

        print(df.head())

        return df