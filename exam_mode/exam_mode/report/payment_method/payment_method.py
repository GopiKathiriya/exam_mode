# Copyright (c) 2023, frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns,data

    

def get_columns():
    columns = [
        {
            'fieldname': 'payment_method',
            'label': 'Payment Method',
            'fieldtype': 'Select',
            'options': ['Cash On Delivery','Online']
        },
        {
            'fieldname': 'test_type',
            'label': 'Test Type',
            'fieldtype': 'Select',
            'options':['Blood Test','X-ray','MRI','Diabetes']
        },
    ]
    return columns

def get_data(filters=None):
    filter_list = []

    
    if filters and filters.get("payment_method"):
        filter_list.append(["payment_method", "=", filters["payment_method"]])

    
    if filters and filters.get("test_type"):
        filter_list.append(["test_type", "=", filters["test_type"]])

    data = frappe.get_list("Fee Collection", filters=filter_list, fields=["payment_method", "test_type"])
    return data