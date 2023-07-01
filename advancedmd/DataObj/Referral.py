from typing import List, Optional
import json

class Referral:
    def __init__(self, referral_date: str, referred_to: str, reason_for_referral: str, patient_id: str, referral_notes: Optional[str] = None):
        self.referral_date = referral_date
        self.referred_to = referred_to
        self.reason_for_referral = reason_for_referral
        self.patient_id = patient_id
        self.referral_notes = referral_notes

    def to_json(self):
        referral_dict = {
            "referral_date": self.referral_date,
            "referred_to": self.referred_to,
            "reason_for_referral": self.reason_for_referral,
            "patient_id": self.patient_id,
            "referral_notes": self.referral_notes
        }
        return json.dumps(referral_dict)


