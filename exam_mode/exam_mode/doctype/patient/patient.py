# Copyright (c) 2023, frappe and contributors
# For license information, please see license.txt


import frappe
from frappe.model.document import Document

class Patient(Document):
    def validate(self):
        self.compute_age()

    def compute_age(self):
        if self.date_of_birth:
            age_in_days = frappe.utils.date_diff(frappe.utils.today(), self.date_of_birth)
            self.age = age_in_days // 365

    # def before_insert(doc):
    #     if doc.doctype == "Patient":
    #         patient_name = doc.patient_name

       
    #     patient_name_cleaned = ''.join(e for e in patient_name if e.isalnum() or e in ['.', '-'])

    #     email_address = patient_name_cleaned.lower() + "@gmail.com"

    #     user = frappe.new_doc("User")
    #     user.update({
    #         "email": email_address,
    #         "first_name": frappe.utils.get_fullname(patient_name),
    #         "new_password": "Sigzen@123#",
    #         "user_type": "System User"
    #     })

    #     user.insert()
    #     user.add_roles("Patient")
 