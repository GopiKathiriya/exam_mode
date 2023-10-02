// Copyright (c) 2023, frappe and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Payment Method"] = {
	"filters": [
		{
			'fieldname': 'patient_name',
			'label': 'Patient Name',
			'fieldtype': 'Link',
			'options': 'Patient'
		},
		{
			'fieldname': 'payment_method',
			'label': 'Payment Method',
			'fieldtype': 'Select',
			'options': ['By Cash','Online']
		},
		{
			'fieldname': 'test_type',
			'label': 'Test Type',
			'fieldtype': 'Link',
			'options': 'Test Type'
		},

	]
};
