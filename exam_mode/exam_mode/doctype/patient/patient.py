# Copyright (c) 2023, frappe and contributors
# For license information, please see license.txt


import frappe
from frappe.model.document import Document

class Patient(Document):
    pass
    # def before_insert(doc):
    #    if doc.doctype == "Patient":
 
        
    #     patient_name = doc.patient_name
    #     user = frappe.new_doc("User")
    #     user.update({
    #     "email": patient_name + "@gmail.com",
    #     "first_name": frappe.utils.get_fullname(patient_name),
    #     "new_password": "Sigzen@123#",
    #     "user_type":"System User"
        
    #     })
    #     user.insert()
    #     user.add_roles("Patient")


