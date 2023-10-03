
import frappe

@frappe.whitelist()
def get_permission_query_for_patient(user=None):
    if not user:
        user = frappe.session.user
    name = frappe.get_value("User", user, "full_name")
    user_roles = frappe.get_roles(user)
    
    if user != 'Administrator' and 'Patient' in user_roles:
        conditions = """(`tabPatient`.patient_name = '{name}')""".format(name=name)
        return conditions
    else:
        pass


@frappe.whitelist()
def get_permission_query_for_testresult(user=None):
    if not user:
        user = frappe.session.user

    if 'Administrator' in frappe.get_roles(user):
        return None

    if 'Patient' in frappe.get_roles(user):
        return """`tabTest Result`.owner = '{user}'""".format(user=user)

    return """1 = 0"""  
 




def user_name(user):
 doc=frappe.get_doc("User",user)
 full_name=doc.full_name
 return full_name