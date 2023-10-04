// Copyright (c) 2023, frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Examination', {
	refresh: function(frm) {
        if (frm.doc.__islocal) {
            frm.page.clear_inner_toolbar();
            
        } else {
            frm.add_custom_button(__('Go To Test Result'), function() {
                var new_test_result = frappe.model.get_new_doc("Test Result");
                new_test_result.patient_name = frm.doc.patient_name;
				new_test_result.test_type = frm.doc.test_type;
				
				
                frappe.set_route("Form", "Test Result", new_test_result.name);
            });
        }
    }
});
