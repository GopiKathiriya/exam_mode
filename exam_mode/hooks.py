from . import __version__ as app_version

app_name = "exam_mode"
app_title = "exam_mode"
app_publisher = "frappe"
app_description = "exam_mode"
app_email = "frappe@gmail.com"
app_license = "MIT"
app_logo_url = "/assets/exam_mode/img/aaaa.jpg"
# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/exam_mode/css/exam_mode.css"
# app_include_js = "/assets/exam_mode/js/exam_mode.js"

# include js, css files in header of web template
# web_include_css = "/assets/exam_mode/css/exam_mode.css"
# web_include_js = "/assets/exam_mode/js/exam_mode.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "exam_mode/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "exam_mode.utils.jinja_methods",
#	"filters": "exam_mode.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "exam_mode.install.before_install"
# after_install = "exam_mode.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "exam_mode.uninstall.before_uninstall"
# after_uninstall = "exam_mode.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "exam_mode.utils.before_app_install"
# after_app_install = "exam_mode.utils.after_app_install"


fixtures = [
    {
        "dt": "Custom DocPerm",
        "filter": [
            ["role", "in", ["Doctor", "Patient", "Receptionist"]],
            ["parent", "in", ["Patient", "Exam Schedule", "Fee Collection","Assign Examiner","Exam Result","Grading Scale","Doctor","Medical Staff","Feedback Form"]]
        ]
    },
    {
        "dt": "Website Slideshow"
    },
    {
        "dt":"Test Type"
    },
    {
        "dt":"Test Investigation"
    },
    {
        "dt": "Website Settings"
    },
    {
        "dt": "Web Page"
    },
    {
        "dt": "Workflow State"
    },
 
    {
        "dt": "Dashboard"
        
    }
]





# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "exam_mode.utils.before_app_uninstall"
# after_app_uninstall = "exam_mode.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "exam_mode.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

permission_query_conditions = {
	"Patient": "exam_mode.permission.patient.get_permission_query_for_patient",
}
{
    "Test Result": "exam_mode.permission.patient.get_permission_query_for_testresult",
}
{
    "Examination": "exam_mode.permission.patient.get_permission_query_for_examination",
}

#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#     "Payment Method": {
#         "before_save": "exam_mode.exam_mode.doctype.payment_method.payment_method.before_save"
#     }
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"exam_mode.tasks.all"
#	],
#	"daily": [
#		"exam_mode.tasks.daily"
#	],
#	"hourly": [
#		"exam_mode.tasks.hourly"
#	],
#	"weekly": [
#		"exam_mode.tasks.weekly"
#	],
#	"monthly": [
#		"exam_mode.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "exam_mode.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "exam_mode.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "exam_mode.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["exam_mode.utils.before_request"]
# after_request = ["exam_mode.utils.after_request"]

# Job Events
# ----------
# before_job = ["exam_mode.utils.before_job"]
# after_job = ["exam_mode.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"exam_mode.auth.validate"
# ]
