from data_generator.generator.generate_patients import PatientGenerator

generator =PatientGenerator()

generator.generate_incremental(
    20001,
    100,
    "output/raw/patients_increment_001.csv"   
)