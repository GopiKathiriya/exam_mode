// Copyright (c) 2023, frappe and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Summary report"] = {
	"filters": [

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
};
