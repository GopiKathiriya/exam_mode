// Copyright (c) 2023, frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Exam Schedule', {
	refresh: function(frm) {
		frm.add_custom_button('Go To Exam Result', () => {
			frappe.new_doc('Exam Result', {
				patient: frm.doc.name 
			});
		});

	}
});
