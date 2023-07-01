from advancedmd import Referral
from advancedmd.UI import Table


# Assuming you have a list of Referral objects
referrals = [
    Referral(referral_date="2023-06-19", referred_to="Specialist", reason_for_referral="Further evaluation"),
    Referral(referral_date="2023-06-20", referred_to="Therapist", reason_for_referral="Counseling"),
    Referral(referral_date="2023-06-21", referred_to="Surgeon", reason_for_referral="Surgery")
]

# Create a Table instance and add the necessary columns
table = Table(referrals)
table.add_column("referral_date", [referral.referral_date for referral in referrals])
table.add_column("referred_to", [referral.referred_to for referral in referrals])
table.add_column("reason_for_referral", [referral.reason_for_referral for referral in referrals])

# Get the markdown representation of the table
markdown_table = table.to_markdown()
print(markdown_table)