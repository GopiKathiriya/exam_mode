frappe.ui.form.on('Patient', {
    refresh: function(frm) {
        frm.fields_dict['date_of_birth'].df.onchange = function() {
            var date_of_birth = frm.doc.date_of_birth;
            if (date_of_birth) {	
                var today = new Date();
                var birthDate = new Date(date_of_birth);
                var ageDate = new Date(today - birthDate);
                var years = ageDate.getUTCFullYear() - 1970;
                var months = ageDate.getUTCMonth();
                var days = ageDate.getUTCDate() - 1;

                frm.set_value('age', years + ' years, ' + months + ' months, ' + days + ' days');
            }
        }
    }
});
