from data_generator.generator.generate_patients import PatientGenerator

generator=PatientGenerator()
generator.generate_incremental(
    10001,
    100,
    "output/raw/patients_duplicate_001.csv"   
)