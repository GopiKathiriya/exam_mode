# Copyright (c) 2023, frappe and contributors
# For license information, please see license.txt


import frappe
from frappe.model.document import Document
from frappe import throw
class Patient(Document):
    def validate(self):
        today = frappe.utils.today()
        
        if self.date_of_birth > today:
            frappe.throw("Date of birth cannot be in the future.")
        
        self.compute_age()

    def compute_age(self):
        if self.date_of_birth:
            age_in_days = frappe.utils.date_diff(frappe.utils.today(), self.date_of_birth)
            self.age = age_in_days // 365

    

   
    def before_insert(doc, method=None):
        if doc.doctype == "Patient":
            patient_name = doc.patient_name
            email = patient_name.replace(" ", "") + "@gmail.com"    
            user = frappe.new_doc("User")
            user.update({
                "email": email,
                "first_name": patient_name,
                "new_password": "Sigzen@123#",
                "user_type": "System User",
                # "role_profile_name":"patient role profile",
                # "module_profile":"exam_mode_profile"
            })
            # user.save(ignore_permissions=True)
            user.add_roles("Patient")
            # user.save(ignore_permissions=True)