import frappe
from frappe import _

def execute(filters=None):
    columns = get_columns()
    data = get_data()
  
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
        {
            'fieldname': 'time_of_test',
            'label': 'Test Of Time',
            'fieldtype': 'Time'
        },
       
    ]
    return columns

def get_data():
   

    data = frappe.db.get_list("Exam Schedule", fields=["patient_name","test_type","time_of_test"])
  

    return data