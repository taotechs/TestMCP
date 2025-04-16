from datetime import datetime
import requests
from typing import Optional, Dict
from .protocols import PatientDataProtocol, StorageProtocol

class MedicalDeviceAPI(PatientDataProtocol):
    """Context implementation for real medical device data"""
    def __init__(self, api_key: str, base_url: str, storage: StorageProtocol):
        self.api_key = api_key
        self.base_url = base_url
        self.storage = storage
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

    def get_vital_signs(self, patient_id: str) -> dict:
        """Get real-time vital signs from medical device"""
        try:
            # Make API call to medical device endpoint
            response = requests.get(
                f"{self.base_url}/patients/{patient_id}/vitals",
                headers=self.headers
            )
            response.raise_for_status()
            
            vital_data = response.json()
            
            # Transform the data to match our expected format
            formatted_data = {
                "temperature": vital_data.get("temp_celsius"),
                "heart_rate": vital_data.get("hr_bpm"),
                "blood_pressure_systolic": vital_data.get("bp_systolic"),
                "blood_pressure_diastolic": vital_data.get("bp_diastolic"),
                "oxygen_saturation": vital_data.get("spo2_percent"),
                "timestamp": datetime.fromisoformat(vital_data.get("measurement_time"))
            }
            
            # Cache the data
            self.storage.store(f"vitals_{patient_id}", formatted_data)
            return formatted_data
            
        except requests.RequestException as e:
            # Fallback to cached data if available
            cached_data = self.storage.retrieve(f"vitals_{patient_id}")
            if cached_data:
                return cached_data
            raise ConnectionError(f"Failed to get vital signs: {str(e)}")

    def save_vital_signs(self, patient_id: str, vital_signs: dict) -> bool:
        """Save vital signs to medical device system"""
        try:
            # Transform our format to the API's expected format
            api_data = {
                "temp_celsius": vital_signs["temperature"],
                "hr_bpm": vital_signs["heart_rate"],
                "bp_systolic": vital_signs["blood_pressure_systolic"],
                "bp_diastolic": vital_signs["blood_pressure_diastolic"],
                "spo2_percent": vital_signs["oxygen_saturation"],
                "measurement_time": vital_signs["timestamp"].isoformat()
            }
            
            # Make API call to save data
            response = requests.post(
                f"{self.base_url}/patients/{patient_id}/vitals",
                headers=self.headers,
                json=api_data
            )
            response.raise_for_status()
            
            # Cache the data locally
            self.storage.store(f"vitals_{patient_id}", vital_signs)
            return True
            
        except requests.RequestException as e:
            print(f"Failed to save vital signs: {str(e)}")
            return False
