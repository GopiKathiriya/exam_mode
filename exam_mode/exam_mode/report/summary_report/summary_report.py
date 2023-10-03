import frappe
from frappe import _

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
  
    return columns, data
   

def get_columns():
    columns = [
        {
             'fieldname': 'patient_name',
            'label': 'Patinet Name',
            'fieldtype': 'Link',
            'options': 'Patient'
        },
        {
            'fieldname': 'test_type',
            'label': 'Test Type',
            'fieldtype': 'Link',
            'options': 'Test Type'
           
        },
        
       
    ]
    return columns

def get_data(filters=None):
    filter_list = []

    if filters and filters.get("patient_name"):
        filter_list.append(["patient_name", "=", filters["patient_name"]])


    if filters and filters.get("test_type"):
        filter_list.append(["test_type", "=", filters["test_type"]])

        
    data = frappe.get_list("Examination",filters=filter_list, fields=["patient_name","test_type"])
  

    return data