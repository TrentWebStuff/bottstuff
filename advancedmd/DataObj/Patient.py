from typing import List, Optional
from advancedmd.DataObj.Visit import Visit
from advancedmd.DataObj.Referral import Referral
from advancedmd.DataObj.ContactInformation import ContactInformation


class Patient:
    def __init__(self, patient_id: str, first_name: str, last_name: str, date_of_birth: str, gender: str,
                 contact_information: ContactInformation, medical_history: List[Visit], referrals: List[Referral]):
        self.patient_id = patient_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.contact_information = contact_information
        self.medical_history = medical_history
        self.referrals = referrals

    def add_referral(self, referral: Referral):
        self.referrals.append(referral)

    def update_referral(self, index: int, updated_referral: Referral):
        if 0 <= index < len(self.referrals):
            self.referrals[index] = updated_referral

    def remove_referral(self, index: int):
        if 0 <= index < len(self.referrals):
            del self.referrals[index]

    def get_referrals(self):
        return self.referrals

    def get_referrals_count(self) -> int:
        return len(self.referrals)
    

    def add_visit(self, visit: Visit):
        self.medical_history.append(visit)

    def update_visit(self, index: int, updated_visit: Visit):
        if 0 <= index < len(self.medical_history):
            self.medical_history[index] = updated_visit

    def remove_visit(self, index: int):
        if 0 <= index < len(self.medical_history):
            del self.medical_history[index]

    def get_visits(self):
        return self.visits
    
    def get_latest_visit(self) -> Optional[Visit]:
        if self.medical_history:
            return self.medical_history[-1]  # Returns the last visit in the medical history
        else:
            return None


    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_age(self) -> int:
        # Calculate the age based on the date_of_birth attribute
        # You can use a date/time library like datetime to perform the calculation
        # Here's an example using the dateutil library:
        import datetime
        from dateutil import parser

        dob = parser.parse(self.date_of_birth)
        now = datetime.datetime.now()
        age = now.year - dob.year - ((now.month, now.day) < (dob.month, dob.day))
        return age

  

