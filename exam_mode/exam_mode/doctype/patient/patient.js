// Copyright (c) 2023, frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Patient', {
	// refresh: function(frm) {
    //     if (frm.doc.__islocal) {
    //         frm.page.clear_inner_toolbar();
    //     } else {
    //         frm.add_custom_button(__('Go To Exam Schedule'), function() {
    //             var new_exam_schedule= frappe.model.get_new_doc("Exam Schedule");
    //             new_exam_schedule.patient_name = frm.doc.patient_name;
				
				
    //             frappe.set_route("Form", "Exam Schedule", new_exam_schedule.name);
    //         });
    //     }
    
});
