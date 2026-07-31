from faker import Faker #type:ignore
import random

FAKER = Faker("en_US")

# Makes data reproducible
Faker.seed(42)
random.seed(42)

GENDERS = [
    "Male",
    "Female"
]

DATE_FORMAT = "%Y-%m-%d"

HOSPITAL_TYPES = [
    "Academic Medical Center",
    "Community Hospital",
    "Children Hospital",
    "Cancer Center",
    "Cardiology Center",
    "Orthopedic Hospital",
    "Rehabilitation Center",
    "Women's Hospital",
    "General Hospital"
]

REGIONS = [
    "Northeast",
    "South",
    "Midwest",
    "West"
]

TRAUMA_LEVEL = [
    "Level I",
    "Level II",
    "Level III",
    "Level IV",
    "None"
]

SPECIALTIES = [
    "Cardiology",
    "Neurology",
    "Orthopedics",
    "Pediatrics",
    "Oncology",
    "Dermatology",
    "Family Medicine",
    "Internal Medicine",
    "Emergency Medicine",
    "Radiology",
    "General Surgery",
    "Psychiatry",
    "Pulmonology",
    "Nephrology",
    "Endocrinology",
    "Rheumatology",
    "Obstetrics & Gynecology",
    "Urology"
]


BOOLEAN_VALUES = [
    True,
    False
]


PLAN_TYPES = [
    "Commercial",
    "Medicare",
    "Medicaid",
    "PPO",
    "HMO",
    "EPO",
    "POS"
]

PLAN_COMPANIES = [
    "Aetna",
    "Cigna",
    "United Healthcare",
    "Blue Cross",
    "Humana",
    "Kaiser",
    "Molina",
    "Centene",
    "Anthem",
    "WellCare"
]

NETWORK_TYPES = [
    "In Network",
    "Out of Network"
]

STATE_CODES = [
    "CA","TX","FL","NY","AZ",
    "GA","NC","WA","NV","CO",
    "IL","OH","PA","MI","TN"
]

DIAGNOSIS_MASTER = [

    ("I10","Essential Hypertension","Cardiology"),
    ("I11.9","Hypertensive Heart Disease","Cardiology"),
    ("I25.10","Coronary Artery Disease","Cardiology"),

    ("E11.9","Type 2 Diabetes","Endocrinology"),
    ("E10.9","Type 1 Diabetes","Endocrinology"),
    ("E78.5","Hyperlipidemia","Endocrinology"),

    ("J45.909","Asthma","Pulmonology"),
    ("J18.9","Pneumonia","Pulmonology"),
    ("J44.9","COPD","Pulmonology"),

    ("M54.5","Low Back Pain","Orthopedics"),
    ("M17.11","Knee Osteoarthritis","Orthopedics"),

    ("G43.909","Migraine","Neurology"),
    ("G40.909","Epilepsy","Neurology"),

    ("C50.919","Breast Cancer","Oncology"),
    ("C34.90","Lung Cancer","Oncology"),

    ("N18.9","Chronic Kidney Disease","Nephrology"),

    ("K21.9","GERD","Gastroenterology"),

    ("F41.1","Generalized Anxiety Disorder","Psychiatry"),

    ("F32.9","Major Depression","Psychiatry")
]

PROCEDURE_MASTER = [

("99213","Office Visit","Family Medicine",120),
("99214","Established Patient Visit","Family Medicine",180),

("93000","Electrocardiogram","Cardiology",220),
("93306","Echocardiogram","Cardiology",650),

("71046","Chest X-Ray","Radiology",180),
("70553","MRI Brain","Radiology",2100),

("80053","Comprehensive Metabolic Panel","Laboratory",90),
("83036","HbA1c","Laboratory",75),

("20610","Joint Injection","Orthopedics",400),
("73562","Knee X-Ray","Orthopedics",250),

("45378","Colonoscopy","Gastroenterology",1800),

("66984","Cataract Surgery","Ophthalmology",4200),

("36415","Blood Collection","Laboratory",35),

("12001","Simple Wound Repair","Emergency Medicine",450),

("11721","Nail Debridement","Podiatry",130)
]

MEDICATION_MASTER = [
("Metformin","Glucophage","Endocrinology"),
("Lisinopril","Prinivil","Cardiology"),
("Atorvastatin","Lipitor","Cardiology"),
("Losartan","Cozaar","Cardiology"),
("Amlodipine","Norvasc","Cardiology"),
("Albuterol","Ventolin","Pulmonology"),
("Prednisone","Deltasone","Pulmonology"),
("Amoxicillin","Amoxil","Antibiotic"),
("Azithromycin","Zithromax","Antibiotic"),
("Ibuprofen","Advil","Pain Management"),
("Acetaminophen","Tylenol","Pain Management"),
("Insulin Glargine","Lantus","Endocrinology"),
("Levothyroxine","Synthroid","Endocrinology"),
("Omeprazole","Prilosec","Gastroenterology"),
("Gabapentin","Neurontin","Neurology"),
("Sertraline","Zoloft","Psychiatry"),
("Fluoxetine","Prozac","Psychiatry"),
("Hydrocodone","Vicodin","Pain Management"),
("Morphine","MS Contin","Pain Management"),
("Warfarin","Coumadin","Cardiology")
]
DOSAGE_FORMS = [
    "Tablet",
    "Capsule",
    "Injection",
    "Liquid",
    "Cream",
    "Inhaler"
]

ROUTES = [
    "Oral",
    "IV",
    "IM",
    "Topical",
    "Inhalation"
]

STRENGTHS = [
    "5 mg",
    "10 mg",
    "20 mg",
    "50 mg",
    "100 mg",
    "250 mg",
    "500 mg"
]

MANUFACTURERS = [
    "Pfizer",
    "Novartis",
    "Merck",
    "AbbVie",
    "Johnson & Johnson",
    "AstraZeneca",
    "GSK",
    "Sanofi",
    "Bayer"
]

PROVIDER_DEPARTMENT = {

    "Cardiology":"Cardiology",

    "Neurology":"Neurology",

    "Orthopedics":"Orthopedics",

    "Pulmonology":"Pulmonology",

    "Oncology":"Oncology",

    "Family Medicine":"Primary Care",

    "Emergency Medicine":"Emergency",

    "Internal Medicine":"Internal Medicine",

    "Radiology":"Radiology",

    "Pediatrics":"Pediatrics"

}

DIAGNOSIS_MAPPING={

"Cardiology":[
"I10",
"I11.9",
"I25.10"
],

"Neurology":[
"G43.909",
"G40.909"
],

"Orthopedics":[
"M54.5",
"M17.11"
],

"Pulmonology":[
"J45.909",
"J44.9",
"J18.9"
],

"Oncology":[
"C50.919",
"C34.90"
],

"Endocrinology":[
"E11.9",
"E10.9"
]
}

PROCEDURE_MAPPING={

"Cardiology":[
"93000",
"93306"
],

"Orthopedics":[
"20610",
"73562"
],

"Pulmonology":[
"71046"
],

"Laboratory":[
"80053",
"83036"
],

"Emergency Medicine":[
"12001"
]

}
#appointment types
VISIT_TYPES = [
    "Outpatient",
    "Emergency",
    "Inpatient"
]

VISIT_TYPE_WEIGHTS = [
    70,
    15,
    15
]

APPOINTMENT_STATUS = [
    "Completed",
    "Cancelled",
    "No Show",
    "Rescheduled"
]

APPOINTMENT_STATUS_WEIGHTS = [
    82,
    8,
    5,
    5
]

PRIORITY = [
    "Low",
    "Medium",
    "High",
    "Critical"
]

PRIORITY_WEIGHTS = [
    45,
    35,
    15,
    5
]

BUSINESS_START_HOUR = 8

BUSINESS_END_HOUR = 18

#claims constant 
CLAIM_STATUS = [
    "Paid",
    "Pending",
    "Denied",
    "Partial Paid"
]

CLAIM_STATUS_WEIGHTS = [
    70,
    15,
    10,
    5
]

COVERAGE_PERCENTAGES = [
    70,
    80,
    90
]

DENIAL_REASONS = [
    "Duplicate Claim",
    "Coverage Expired",
    "Missing Documentation",
    "Invalid Procedure Code",
    "Medical Necessity Not Met",
    "Prior Authorization Required"
]

#Claim line 

LINE_STATUS = [
    "Approved",
    "Pending",
    "Denied"
]

LINE_STATUS_WEIGHTS = [
    80,
    10,
    10
]

MIN_LINE_ITEMS = 1

MAX_LINE_ITEMS = 5

#payment methods
PAYMENT_METHODS = [
    "Credit Card",
    "Cash",
    "Bank Transfer",
    "Insurance EFT",
    "Cheque"
]

PAYMENT_STATUS = [
    "Paid",
    "Partial Paid",
    "Pending",
    "Failed"
]

PAYMENT_STATUS_WEIGHTS = [
    75,
    10,
    10,
    5
]

#Presciption constants
PRESCRIPTION_STATUS = [
    "Active",
    "Completed",
    "Cancelled"
]

PRESCRIPTION_STATUS_WEIGHTS = [
    75,
    20,
    5
]

DOSAGE_FREQUENCY = [
    "Once Daily",
    "Twice Daily",
    "Three Times Daily",
    "Every 6 Hours",
    "Every 8 Hours",
    "As Needed"
]

DURATION_DAYS = [
    5,
    7,
    10,
    14,
    30,
    60,
    90
]


#Lab_Result_Constant
LAB_TESTS = [
    {
        "Test_Name": "Hemoglobin",
        "Unit": "g/dL",
        "Min": 13.0,
        "Max": 17.0
    },
    {
        "Test_Name": "HbA1c",
        "Unit": "%",
        "Min": 4.0,
        "Max": 5.6
    },
    {
        "Test_Name": "Blood Glucose",
        "Unit": "mg/dL",
        "Min": 70,
        "Max": 99
    },
    {
        "Test_Name": "Total Cholesterol",
        "Unit": "mg/dL",
        "Min": 120,
        "Max": 200
    },
    {
        "Test_Name": "White Blood Cell",
        "Unit": "10^9/L",
        "Min": 4.5,
        "Max": 11.0
    }
]

RESULT_STATUS = [
    "Normal",
    "High",
    "Low",
    "Critical"
]

RESULT_STATUS_WEIGHTS = [
    75,
    12,
    10,
    3
]

#Encounter Constant 
ENCOUNTER_TYPES = [
    "Outpatient",
    "Inpatient",
    "Emergency",
    "Telehealth",
    "Follow-up"
]

ENCOUNTER_STATUS = [
    "Completed",
    "Cancelled",
    "No Show"
]

ENCOUNTER_STATUS_WEIGHTS = [
    85,
    5,
    10
]

#admission constants

ADMISSION_TYPES = [
    "Emergency",
    "Elective",
    "Urgent",
    "Maternity",
    "Trauma"
]

ADMISSION_STATUS = [
    "Admitted",
    "Transferred",
    "Observation"
]

ADMISSION_STATUS_WEIGHTS = [
    80,
    10,
    10
]

ROOM_TYPES = [
    "General Ward",
    "Semi Private",
    "Private",
    "ICU",
    "CCU"
]

#discharge 
DISCHARGE_DISPOSITION = [
    "Home",
    "Transferred",
    "Rehabilitation",
    "Expired",
    "Left Against Medical Advice"
]

DISCHARGE_DISPOSITION_WEIGHTS = [
    75,
    10,
    10,
    2,
    3
]

#Audit log 
AUDIT_ACTIONS = [
    "INSERT",
    "UPDATE",
    "DELETE"
]

ENTITY_TYPES = [
    "Patient",
    "Appointment",
    "Claim",
    "Prescription",
    "Payment",
    "Encounter"
]

USERS = [
    "System",
    "Doctor",
    "Nurse",
    "Billing",
    "Admin"
]

#constants 
CDC_OPERATIONS = [
    "INSERT",
    "UPDATE",
    "DELETE"
]