import random
import pandas as pd

from faker import Faker

from data_generator.common.writer import CsvWriter
from data_generator.common.conifg_loader import ConfigLoader

from data_generator.common.constants import PROCEDURE_MASTER

fake = Faker()


class ProcedureGenerator:

    def __init__(self):

        config = ConfigLoader.load()

        self.rows = config["procedures"]["rows"]

    def generate(self):

        procedures=[]

        for i in range(self.rows):

            code,name,specialty,cost = random.choice(PROCEDURE_MASTER)

            procedures.append({

                "Procedure_ID":f"PROC{i+1:06}",

                "CPT_Code":code,

                "Procedure_Name":name,

                "Specialty":specialty,

                "Procedure_Cost":cost,

                "Duration_Minutes":
                    random.randint(10,180),

                "Requires_Admission":
                    random.choice(["Yes","No"]),

                "Active":"Yes",

                "Created_Date":
                    fake.date_between("-5y","today")

            })

        df=pd.DataFrame(procedures)

        CsvWriter.write(
            df,
            "output/raw/procedure_codes.csv"
        )

        print(df.head())

        return df