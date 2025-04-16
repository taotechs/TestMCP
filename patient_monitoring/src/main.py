from datetime import datetime, timedelta
from .contexts import InMemoryStorage, SimplePatientData, ConsoleAlertSystem
from .models import PatientMonitor
import time
import random

def generate_vital_signs(patient_condition="normal"):
    """Generate vital signs based on patient condition"""
    if patient_condition == "normal":
        return {
            "temperature": round(random.uniform(36.5, 37.5), 1),
            "heart_rate": random.randint(60, 100),
            "blood_pressure_systolic": random.randint(110, 130),
            "blood_pressure_diastolic": random.randint(70, 85),
            "oxygen_saturation": random.randint(95, 100),
            "timestamp": datetime.now()
        }
    elif patient_condition == "fever":
        return {
            "temperature": round(random.uniform(38.5, 40.0), 1),
            "heart_rate": random.randint(90, 110),
            "blood_pressure_systolic": random.randint(110, 130),
            "blood_pressure_diastolic": random.randint(70, 85),
            "oxygen_saturation": random.randint(93, 97),
            "timestamp": datetime.now()
        }
    elif patient_condition == "critical":
        return {
            "temperature": round(random.uniform(39.0, 41.0), 1),
            "heart_rate": random.randint(120, 150),
            "blood_pressure_systolic": random.randint(160, 180),
            "blood_pressure_diastolic": random.randint(95, 110),
            "oxygen_saturation": random.randint(85, 92),
            "timestamp": datetime.now()
        }

def simulate_patient_monitoring(duration_minutes=10, interval_seconds=30):
    """Simulate patient monitoring for a specified duration"""
    # Initialize contexts
    storage = InMemoryStorage()
    data_provider = SimplePatientData(storage)
    alert_system = ConsoleAlertSystem()

    # Initialize model with contexts
    monitor = PatientMonitor(data_provider, alert_system)

    # Simulate multiple patients with different conditions
    patients = {
        "12345": "normal",
        "12346": "fever",
        "12347": "critical"
    }

    print(f"Starting patient monitoring simulation for {duration_minutes} minutes...")
    start_time = datetime.now()
    end_time = start_time + timedelta(minutes=duration_minutes)

    try:
        while datetime.now() < end_time:
            for patient_id, condition in patients.items():
                # Generate and save vital signs
                vital_signs = generate_vital_signs(condition)
                data_provider.save_vital_signs(patient_id, vital_signs)
                
                # Monitor patient
                print(f"\nChecking patient {patient_id} ({condition} condition):")
                monitor.check_vital_signs(patient_id)

            time.sleep(interval_seconds)

    except KeyboardInterrupt:
        print("\nSimulation stopped by user")

def main():
    # Run simulation for 2 minutes with 30-second intervals
    simulate_patient_monitoring(duration_minutes=2, interval_seconds=30)

if __name__ == "__main__":
    main()
