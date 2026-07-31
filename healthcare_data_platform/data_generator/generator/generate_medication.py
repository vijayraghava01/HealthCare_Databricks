import random
import pandas as pd

from faker import Faker

from data_generator.common.writer import CsvWriter
from data_generator.common.conifg_loader import ConfigLoader

from data_generator.common.constants import (
    MEDICATION_MASTER,
    DOSAGE_FORMS,
    ROUTES,
    STRENGTHS,
    MANUFACTURERS
)
fake = Faker()

class MedicationGenerator:

    def __init__(self):

        config = ConfigLoader.load()

        self.rows = config["medications"]["rows"]

    def generate(self):

        medications=[]

        for i in range(self.rows):

            generic,brand,therapy = random.choice(MEDICATION_MASTER)

            medications.append({

                "Medication_ID":f"MED{i+1:06}",

                "Generic_Name":generic,

                "Brand_Name":brand,

                "Therapeutic_Class":therapy,

                "Strength":random.choice(STRENGTHS),

                "Dosage_Form":random.choice(DOSAGE_FORMS),

                "Route":random.choice(ROUTES),

                "Manufacturer":random.choice(MANUFACTURERS),

                "Unit_Cost":round(random.uniform(5,500),2),

                "Controlled_Substance":
                    random.choice(["Yes","No"]),

                "Requires_Prior_Authorization":
                    random.choice(["Yes","No"]),

                "Active":"Yes",

                "Created_Date":
                    fake.date_between("-5y","today")

            })

        df=pd.DataFrame(medications)

        CsvWriter.write(
            df,
            "output/raw/medications.csv"
        )

        print(df.head())

        return df