// Copyright (c) 2023, frappe and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Payment Method"] = {
	"filters": [
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
			'options':['Blood Test','X-ray','MIR','Diabetes']
		},

	]
};
