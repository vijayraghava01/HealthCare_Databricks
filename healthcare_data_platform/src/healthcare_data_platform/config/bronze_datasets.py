from healthcare_data_platform.config.constants import BRONZE_SCHEMA


BRONZE_DATASETS = {

    "patients": {

        "landing_path": "patients",

        "target_table": "patients",

        "schema": BRONZE_SCHEMA,

        "primary_key": "Patient_ID",

        "partition_columns": [],

        "cdc_enabled": False,

        "masking_required": True,

        "quality_checks": True,

        "schema_hints": """
            Patient_ID STRING,
            MRN STRING,
            First_Name STRING,
            Last_Name STRING,
            DOB DATE,
            Gender STRING,
            Phone STRING,
            Email STRING,
            Address STRING,
            City STRING,
            State STRING,
            Zip_Code INT,
            Created_Date DATE,
            Updated_Date DATE,
            Insurance_Type STRING
        """
    },

    "providers": {
        "landing_path": "providers",
        "target_table": "providers",
        "schema": BRONZE_SCHEMA,
        "primary_key": "provider_id",
        "partition_columns": [],
        "cdc_enabled": False,
        "masking_required": False,
        "quality_checks": True,
    },

    "appointments": {
        "landing_path": "appointments",
        "target_table": "appointments",
        "schema": BRONZE_SCHEMA,
        "primary_key": "appointment_id",
        "partition_columns": [],
        "cdc_enabled": False,
        "masking_required": False,
        "quality_checks": True,
    },

    "admissions": {
        "landing_path": "admissions",
        "target_table": "admissions",
        "schema": BRONZE_SCHEMA,
        "primary_key": "admission_id",
        "partition_columns": [],
        "cdc_enabled": False,
        "masking_required": False,
        "quality_checks": True,
    },

    "audit_logs": {
        "landing_path": "audit_logs",
        "target_table": "audit_logs",
        "schema": BRONZE_SCHEMA,
        "primary_key": "audit_id",
        "partition_columns": [],
        "cdc_enabled": False,
        "masking_required": False,
        "quality_checks": True,
    },

    "cdc_events": {
        "landing_path": "cdc_events",
        "target_table": "cdc_events",
        "schema": BRONZE_SCHEMA,
        "primary_key": "event_id",
        "partition_columns": [],
        "cdc_enabled": True,
        "masking_required": False,
        "quality_checks": True,
    },

    "claim_lines": {
        "landing_path": "claim_lines",
        "target_table": "claim_lines",
        "schema": BRONZE_SCHEMA,
        "primary_key": "claim_line_id",
        "partition_columns": [],
        "cdc_enabled": False,
        "masking_required": False,
        "quality_checks": True,
    },

    "claims": {
        "landing_path": "claims",
        "target_table": "claims",
        "schema": BRONZE_SCHEMA,
        "primary_key": "claim_id",
        "partition_columns": [],
        "cdc_enabled": False,
        "masking_required": False,
        "quality_checks": True,
    },

    "diagnosis_codes": {
        "landing_path": "diagnosis_codes",
        "target_table": "diagnosis_codes",
        "schema": BRONZE_SCHEMA,
        "primary_key": "diagnosis_code",
        "partition_columns": [],
        "cdc_enabled": False,
        "masking_required": False,
        "quality_checks": True,
    },

    "discharges": {
        "landing_path": "discharges",
        "target_table": "discharges",
        "schema": BRONZE_SCHEMA,
        "primary_key": "discharge_id",
        "partition_columns": [],
        "cdc_enabled": False,
        "masking_required": False,
        "quality_checks": True,
    },

    "encounters": {
        "landing_path": "encounters",
        "target_table": "encounters",
        "schema": BRONZE_SCHEMA,
        "primary_key": "encounter_id",
        "partition_columns": [],
        "cdc_enabled": False,
        "masking_required": False,
        "quality_checks": True,
    },

    "hospitals": {
        "landing_path": "hospitals",
        "target_table": "hospitals",
        "schema": BRONZE_SCHEMA,
        "primary_key": "hospital_id",
        "partition_columns": [],
        "cdc_enabled": False,
        "masking_required": False,
        "quality_checks": True,
    },

    "insurance_plans": {
        "landing_path": "insurance_plans",
        "target_table": "insurance_plans",
        "schema": BRONZE_SCHEMA,
        "primary_key": "insurance_plan_id",
        "partition_columns": [],
        "cdc_enabled": False,
        "masking_required": False,
        "quality_checks": True,
    },

    "lab_results": {
        "landing_path": "lab_results",
        "target_table": "lab_results",
        "schema": BRONZE_SCHEMA,
        "primary_key": "lab_result_id",
        "partition_columns": [],
        "cdc_enabled": False,
        "masking_required": False,
        "quality_checks": True,
    },

    "medications": {
        "landing_path": "medications",
        "target_table": "medications",
        "schema": BRONZE_SCHEMA,
        "primary_key": "medication_id",
        "partition_columns": [],
        "cdc_enabled": False,
        "masking_required": False,
        "quality_checks": True,
    },

    "payments": {
        "landing_path": "payments",
        "target_table": "payments",
        "schema": BRONZE_SCHEMA,
        "primary_key": "payment_id",
        "partition_columns": [],
        "cdc_enabled": False,
        "masking_required": False,
        "quality_checks": True,
    },

    "prescriptions": {
        "landing_path": "prescriptions",
        "target_table": "prescriptions",
        "schema": BRONZE_SCHEMA,
        "primary_key": "prescription_id",
        "partition_columns": [],
        "cdc_enabled": False,
        "masking_required": False,
        "quality_checks": True,
    },

    "procedure_codes": {
        "landing_path": "procedure_codes",
        "target_table": "procedure_codes",
        "schema": BRONZE_SCHEMA,
        "primary_key": "procedure_code",
        "partition_columns": [],
        "cdc_enabled": False,
        "masking_required": False,
        "quality_checks": True,
    },
}