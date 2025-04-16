from typing import Protocol, Any
from datetime import datetime

class PatientDataProtocol(Protocol):
    """Protocol defining patient data operations"""
    def get_vital_signs(self, patient_id: str) -> dict:
        """Get patient vital signs"""
        ...

    def save_vital_signs(self, patient_id: str, vital_signs: dict) -> bool:
        """Save patient vital signs"""
        ...

class AlertProtocol(Protocol):
    """Protocol defining alert system operations"""
    def send_alert(self, message: str, severity: str, timestamp: datetime) -> bool:
        """Send an alert"""
        ...

class StorageProtocol(Protocol):
    """Protocol defining data storage operations"""
    def store(self, key: str, value: Any) -> bool:
        """Store data"""
        ...
    
    def retrieve(self, key: str) -> Any:
        """Retrieve data"""
        ...
