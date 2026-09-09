
from data_generator.generator.generate_appointments import AppointmentGenerator
appointmentgenerator=AppointmentGenerator()
appointmentgenerator.generate_incremental(
       1000001,
        100,
        "output/raw/appointments_increment_001.csv"   
)