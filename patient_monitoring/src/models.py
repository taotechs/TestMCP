from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional
from .protocols import PatientDataProtocol, AlertProtocol

class VitalSigns(BaseModel):
    """Model representing patient vital signs"""
    temperature: float = Field(..., ge=35.0, le=43.0)
    heart_rate: int = Field(..., ge=0, le=250)
    blood_pressure_systolic: int = Field(..., ge=0, le=300)
    blood_pressure_diastolic: int = Field(..., ge=0, le=200)
    oxygen_saturation: int = Field(..., ge=0, le=100)
    timestamp: datetime

class PatientMonitor:
    """Model implementing patient monitoring logic"""
    def __init__(self, data_provider: PatientDataProtocol, alert_system: AlertProtocol):
        self.data_provider = data_provider
        self.alert_system = alert_system

    def check_vital_signs(self, patient_id: str) -> bool:
        """Check if patient vital signs are within normal ranges"""
        vital_data = self.data_provider.get_vital_signs(patient_id)
        vitals = VitalSigns(**vital_data)
        
        # Check for critical conditions
        if vitals.temperature > 39.5:  # High fever
            self.alert_system.send_alert(
                f"High fever detected for patient {patient_id}: {vitals.temperature}°C",
                "HIGH",
                vitals.timestamp
            )
            return False
            
        if vitals.oxygen_saturation < 90:  # Low oxygen
            self.alert_system.send_alert(
                f"Low oxygen saturation for patient {patient_id}: {vitals.oxygen_saturation}%",
                "HIGH",
                vitals.timestamp
            )
            return False

        if vitals.heart_rate > 120 or vitals.heart_rate < 50:  # Abnormal heart rate
            self.alert_system.send_alert(
                f"Abnormal heart rate for patient {patient_id}: {vitals.heart_rate} BPM",
                "MEDIUM",
                vitals.timestamp
            )
            return False

        return True
