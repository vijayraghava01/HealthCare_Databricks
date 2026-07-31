import pandas as pd

from data_generator.common.data_loader import DataLoader
from data_generator.common.writer import CsvWriter


class AppointmentBadGenerator:

    def generate(self):

        appointments = DataLoader.load_csv(
            "output/raw/appointments.csv"
        )

        bad = appointments.sample(
            frac=0.02,
            random_state=42
        ).copy().reset_index(drop=True)

        # Duplicate Appointment_ID
        bad.loc[0, "Appointment_ID"] = appointments.iloc[1]["Appointment_ID"]

        # Invalid Patient_ID
        bad.loc[1, "Patient_ID"] = "P999999"

        # Invalid Provider_ID
        bad.loc[2, "Provider_ID"] = "PR999999"

        # Future Appointment Date
        bad.loc[3, "Appointment_Date"] = "2050-01-01"

        # Invalid Status
        bad.loc[4, "Appointment_Status"] = "UNKNOWN"

        # Null Hospital_ID
        bad.loc[5, "Hospital_ID"] = None

        # Null Diagnosis_ID
        bad.loc[6, "Diagnosis_ID"] = None

        # Null Appointment Date
        bad.loc[7, "Appointment_Date"] = None

        # Invalid Priority
        if "Priority" in bad.columns:
            bad.loc[8, "Priority"] = "SUPER HIGH"

        CsvWriter.write(
            bad,
            "output/bad_data/appointments_bad.csv"
        )

        print(
            f"Generated {len(bad)} Bad Appointment Records"
        )

        return bad