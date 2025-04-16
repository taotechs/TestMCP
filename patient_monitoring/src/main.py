from datetime import datetime
from .contexts import InMemoryStorage, SimplePatientData, ConsoleAlertSystem
from .models import PatientMonitor

def main():
    # Initialize contexts
    storage = InMemoryStorage()
    data_provider = SimplePatientData(storage)
    alert_system = ConsoleAlertSystem()

    # Initialize model with contexts
    monitor = PatientMonitor(data_provider, alert_system)

    # Simulate patient data
    patient_id = "12345"
    vital_signs = {
        "temperature": 39.8,  # High fever
        "heart_rate": 95,
        "blood_pressure_systolic": 120,
        "blood_pressure_diastolic": 80,
        "oxygen_saturation": 88,  # Low oxygen
        "timestamp": datetime.now()
    }

    # Save and check vital signs
    data_provider.save_vital_signs(patient_id, vital_signs)
    monitor.check_vital_signs(patient_id)

if __name__ == "__main__":
    main()
