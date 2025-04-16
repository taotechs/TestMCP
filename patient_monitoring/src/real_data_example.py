from .contexts import InMemoryStorage, ConsoleAlertSystem
from .real_data_contexts import MedicalDeviceAPI
from .models import PatientMonitor
import os
from time import sleep

def main():
    # Initialize contexts
    storage = InMemoryStorage()
    
    # Initialize medical device API context
    # In production, these would come from environment variables or secure configuration
    api_key = os.getenv("MEDICAL_DEVICE_API_KEY", "your-api-key")
    base_url = os.getenv("MEDICAL_DEVICE_API_URL", "https://api.medical-device.example.com/v1")
    
    data_provider = MedicalDeviceAPI(api_key, base_url, storage)
    alert_system = ConsoleAlertSystem()

    # Initialize model with contexts
    monitor = PatientMonitor(data_provider, alert_system)

    # Monitor patients in real-time
    patient_ids = ["12345", "12346", "12347"]  # List of patients to monitor
    
    try:
        while True:
            for patient_id in patient_ids:
                try:
                    # This will automatically fetch real-time data from the medical device
                    monitor.check_vital_signs(patient_id)
                except ConnectionError as e:
                    print(f"Error monitoring patient {patient_id}: {str(e)}")
                
            # Wait for 5 minutes before next check
            sleep(300)
    except KeyboardInterrupt:
        print("\nStopping patient monitoring...")

if __name__ == "__main__":
    main()
