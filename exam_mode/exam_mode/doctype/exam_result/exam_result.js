// Copyright (c) 2023, frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Exam Result', {
	refresh: function(frm) {
		frm.add_custom_button('Go To Fee Collection', () => {
			frappe.new_doc('Fee Collection', {
				patient: frm.doc.name 
			});
		});

	}
});
