from datetime import datetime
from typing import Any, Dict
from .protocols import PatientDataProtocol, AlertProtocol, StorageProtocol

class InMemoryStorage(StorageProtocol):
    """Context implementation for in-memory storage"""
    def __init__(self):
        self._storage: Dict[str, Any] = {}

    def store(self, key: str, value: Any) -> bool:
        self._storage[key] = value
        return True

    def retrieve(self, key: str) -> Any:
        return self._storage.get(key)

class SimplePatientData(PatientDataProtocol):
    """Context implementation for patient data operations"""
    def __init__(self, storage: StorageProtocol):
        self.storage = storage

    def get_vital_signs(self, patient_id: str) -> dict:
        return self.storage.retrieve(f"vitals_{patient_id}") or {}

    def save_vital_signs(self, patient_id: str, vital_signs: dict) -> bool:
        return self.storage.store(f"vitals_{patient_id}", vital_signs)

class ConsoleAlertSystem(AlertProtocol):
    """Context implementation for console-based alerts"""
    def send_alert(self, message: str, severity: str, timestamp: datetime) -> bool:
        print(f"[{severity}] {timestamp.isoformat()}: {message}")
        return True
