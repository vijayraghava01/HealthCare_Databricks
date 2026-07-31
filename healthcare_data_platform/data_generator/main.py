from data_generator.common.orchestrator import GeneratorOrchestrator
from data_generator.generator.generate_patients import PatientGenerator
from data_generator.generator.generate_hospitals import HospitalGenerator
from data_generator.generator.generate_providers import ProviderGenerator
from data_generator.generator.generate_insurance import InsuranceGenerator
from data_generator.generator.generate_diagnosis import DiagnosisGenerator
from data_generator.generator.generate_procedures import ProcedureGenerator
from data_generator.generator.generate_medication import MedicationGenerator
from data_generator.generator.generate_appointments import AppointmentGenerator
from data_generator.generator.generate_claims import ClaimGenerator
from data_generator.generator.generate_claimLine import ClaimLineGenerator
from data_generator.generator.generate_payments import PaymentGenerator
from data_generator.generator.generate_presciption import PrescriptionGenerator
from data_generator.generator.generate_Labresult import LabResultGenerator
from data_generator.generator.generate_encounter import EncounterGenerator
from data_generator.generator.generate_admisson import AdmissionGenerator
from data_generator.generator.generate_discharge import DischargeGenerator
from data_generator.generator.generate_audit import AuditGenerator
from data_generator.generator.generate_cdc import CDCGenerator
from data_generator.bad_generator.patient_bad_generator import PatientBadGenerator
from data_generator.bad_generator.appointment_bad_generator import AppointmentBadGenerator
from data_generator.bad_generator.claim_bad_generator import ClaimBadGenerator
from data_generator.bad_generator.lab_result_bad_generator import LabResultBadGenerator
from data_generator.bad_generator.payment_bad_generator import  PaymentBadGenerator

def main():

    orchestrator = GeneratorOrchestrator()
    orchestrator.register(HospitalGenerator())
    orchestrator.register(ProviderGenerator())
    orchestrator.register(PatientGenerator())
    orchestrator.register(InsuranceGenerator())
    orchestrator.register(DiagnosisGenerator())
    orchestrator.register(ProcedureGenerator())
    orchestrator.register(MedicationGenerator())
    orchestrator.register(AppointmentGenerator())
    orchestrator.register(ClaimGenerator())
    orchestrator.register(ClaimLineGenerator())
    orchestrator.register(PaymentGenerator())
    orchestrator.register(PrescriptionGenerator())
    orchestrator.register(LabResultGenerator())
    orchestrator.register(EncounterGenerator())
    orchestrator.register(AdmissionGenerator())
    orchestrator.register(DischargeGenerator())
    orchestrator.register(AuditGenerator())
    orchestrator.register(CDCGenerator())
    orchestrator.register(PatientBadGenerator())
    orchestrator.register(AppointmentBadGenerator())
    orchestrator.register(ClaimBadGenerator())
    orchestrator.register(LabResultBadGenerator())
    orchestrator.register(PaymentBadGenerator())
    orchestrator.execute()


if __name__ == "__main__":
    main()