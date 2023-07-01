from typing import List, Optional

class ContactInformation:
    def __init__(self, email: str, phone: Optional[str] = None, address: Optional[str] = None):
        self.email = email
        self.phone = phone
        self.address = address

    def update_email(self, new_email: str):
        self.email = new_email

    def update_phone(self, new_phone: str):
        self.phone = new_phone

    def update_address(self, new_address: str):
        self.address = new_address