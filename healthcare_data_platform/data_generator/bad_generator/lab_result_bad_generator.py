import pandas as pd

from data_generator.common.data_loader import DataLoader
from data_generator.common.writer import CsvWriter


class LabResultBadGenerator:

    def generate(self):

        lab_results = DataLoader.load_csv(
            "output/raw/lab_results.csv"
        )

        bad = lab_results.sample(
            frac=0.02,
            random_state=42
        ).copy().reset_index(drop=True)

        # Duplicate Lab_Result_ID
        bad.loc[0, "Lab_Result_ID"] = (
            lab_results.iloc[1]["Lab_Result_ID"]
        )

        # Invalid Patient_ID
        bad.loc[1, "Patient_ID"] = "P999999"

        # Null Test Name
        bad.loc[2, "Test_Name"] = None

        # Negative Result Value
        bad.loc[3, "Result_Value"] = -25

        # Impossible HbA1c Value
        bad.loc[4, "Test_Name"] = "HbA1c"
        bad.loc[4, "Result_Value"] = 52

        # Invalid Result Status
        bad.loc[5, "Result_Status"] = "INVALID"

        # Null Unit
        bad.loc[6, "Unit"] = None

        # Invalid Reference Range
        bad.loc[7, "Reference_Range"] = "ABC"

        # Future Result Date
        bad.loc[8, "Result_Date"] = "2055-01-01"

        # Null Appointment_ID
        bad.loc[9, "Appointment_ID"] = None

        CsvWriter.write(
            bad,
            "output/bad_data/lab_results_bad.csv"
        )

        print(
            f"Generated {len(bad)} Bad Lab Results"
        )

        return bad