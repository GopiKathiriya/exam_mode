// Copyright (c) 2023, frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Test Result', {
    refresh: function(frm) {
        if (frm.doc.__islocal) {
            frm.page.clear_inner_toolbar();
        } else {
            frm.add_custom_button(__('Go To Payment'), function() {
                var new_payment_method = frappe.model.get_new_doc("Payment Method");
                new_payment_method.patient_name = frm.doc.patient_name;
                new_payment_method.test_type = frm.doc.test_type;
                frappe.set_route("Form", "Payment Method", new_payment_method.name);
            });
        }
    },
    test_type: function (frm) {
        console.log("hey");
        if (frm.doc.test_type) {
            frappe.call({
                method: "exam_mode.exam_mode.doctype.test_result.test_result.test_type",
                args: {
                    test_type: frm.doc.test_type
                },
                callback: function (r) {
                    if (r.message) {
                        frm.clear_table("test");
                        r.message.forEach(function (i) {
                            console.log(i);
                            var row = frm.add_child('test', {
                                investigation: i.investigation,
                                reference_value: i.reference_value,
                                grading_scale: i.grading_scale
                            });
                        });
                        frm.refresh_field("test");
                    }
                }
            });
        }
    } 
});
