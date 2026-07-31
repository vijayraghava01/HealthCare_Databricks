import random

import pandas as pd

from data_generator.common.data_loader import DataLoader
from data_generator.common.writer import CsvWriter


class PatientBadGenerator:

    def generate(self):

        patients = DataLoader.load_csv(
            "output/raw/patients.csv"
        )

        bad = patients.sample(
            frac=0.02,
            random_state=42
        ).copy()

        # Duplicate Patient_ID
        bad.loc[0, "Patient_ID"] = patients.iloc[1]["Patient_ID"]

        # Null First Name
        bad.loc[1, "First_Name"] = None

        # Future DOB
        bad.loc[2, "DOB"] = "2055-01-01"

        # Invalid Email
        bad.loc[3, "Email"] = "abc@@gmail"

        # Invalid State
        bad.loc[4, "State"] = "XXXXX"

        # Null Phone
        bad.loc[5, "Phone"] = None

        CsvWriter.write(
            bad,
            "output/bad_data/patients_bad.csv"
        )

        print(
            f"Generated {len(bad)} Bad Patient Records"
        )

        return bad