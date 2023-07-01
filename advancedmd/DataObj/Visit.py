from typing import List, Optional
import json

class Visit:
    def __init__(self, visit_date: str, symptoms: list[str], diagnosis: list[str], treatment: str, doctor: str, notes: Optional[str] = None):
        self.visit_date = visit_date
        self.symptoms = symptoms
        self.diagnosis = diagnosis
        self.treatment = treatment
        self.doctor = doctor
        self.notes = notes

    def add_symptom(self, symptom: str):
        self.symptoms.append(symptom)

    def remove_symptom(self, symptom: str):
        if symptom in self.symptoms:
            self.symptoms.remove(symptom)
    

    def to_json(self):
        visit_dict = {
            "visit_date": self.visit_date,
            "symptoms": self.symptoms,
            "diagnosis": self.diagnosis,
            "treatment": self.treatment,
            "doctor": self.doctor,
            "notes": self.notes
        }
        return json.dumps(visit_dict)