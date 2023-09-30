// Copyright (c) 2023, frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Test Result', {
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
                        r.message.forEach(function (i) {
                            console.log(i);
                            frm.add_child('test', {
                                investigation: i.investigation,
								reference_value: i.reference_value
                            });
                        });
                        frm.refresh_field("test");
                    }
                }
            });
        }
    }
});
