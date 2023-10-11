frappe.ui.form.on('Exam Schedule', {
    refresh: function(frm) {
        if (frm.doc.__islocal) {
            frm.page.clear_inner_toolbar();
        } else {
            if (frappe.user.has_role('Doctor')&& frm.doc.docstatus === 1) {

            frm.add_custom_button(__('Go To Examination'), function() {
                var new_examination = frappe.model.get_new_doc("Examination");
                new_examination.patient_name = frm.doc.patient_name;
                new_examination.test_type = frm.doc.test_type;
				new_examination.doctor = frm.doc.assign_doctor;
				
                frappe.set_route("Form", "Examination", new_examination.name);
            });
        }
    }
}
});
