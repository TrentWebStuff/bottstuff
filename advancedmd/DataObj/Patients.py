import json
from advancedmd.DataObj.Visit import Visit
from advancedmd.DataObj.Referral import Referral
from advancedmd.DataObj.ContactInformation import ContactInformation
from advancedmd.DataObj.Patient import Patient


class Patients:
    def __init__(self, json_url: str):
        self.patients = self.load_patients_from_json(json_url)



    def load_patients_from_json(self, json_url: str):
        patients = []

        # Read the JSON file
        with open(json_url, 'r') as file:
            data = json.load(file)

        # Create patient instances from the JSON data
        for patient_data in data['patients']:
            contact_information_data = patient_data['contactInformation']
            contact_information = ContactInformation(contact_information_data['email'], contact_information_data.get('phone'), contact_information_data.get('address'))

            medical_history_data = patient_data['medicalHistory']
            medical_history = []
            for visit_data in medical_history_data:
                visit = Visit(visit_data['visitDate'], visit_data['symptoms'], visit_data['diagnosis'], visit_data['treatment'], visit_data['doctor'], visit_data.get('notes'))
                medical_history.append(visit)

            referrals_data = patient_data['referrals']
            referrals = []
            for referral_data in referrals_data:
                referral = Referral(referral_data['referralDate'], referral_data['referredTo'], referral_data['reasonForReferral'], patient_data['patientId'], referral_data.get('referralNotes'))
                referrals.append(referral)

            patient = Patient(patient_data['patientId'], patient_data['firstName'], patient_data['lastName'], patient_data['dateOfBirth'], patient_data['gender'], contact_information, medical_history, referrals)
            patients.append(patient)

        return patients
    

    def get_all_referrals(self):
        all_referrals = []
        for patient in self.patients:
            all_referrals.extend(patient.get_referrals())
        return all_referrals


