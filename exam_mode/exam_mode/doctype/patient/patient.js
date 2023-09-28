// Copyright (c) 2023, frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Patient', {
	refresh: function(frm) {
		frm.add_custom_button('Go To Exam Schedule', () => {
			frappe.new_doc('Exam Schedule', {
				patient: frm.doc.name 
			});
		});

	}
});
