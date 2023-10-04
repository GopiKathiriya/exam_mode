
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
        user_roles = frappe.get_roles(user)
    if user != 'Administrator' and 'Patient' in user_roles:
    
        conditions=""" (`tabTest Result`.owner = '{user}')""".format(user=user)
        return conditions
    else:
        pass

@frappe.whitelist()
def get_permission_query_for_examination(user=None):
   if not user:
      user = frappe.session.user
      user_roles = frappe.get_roles(user)
   if user != 'Administrator' and 'Patient' in user_roles:
      conditions=""" (`tabExamination`.owner = '{user}')""".format(user=user)
      return conditions
   else:
      pass
 
     
    



