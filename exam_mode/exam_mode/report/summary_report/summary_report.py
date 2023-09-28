import frappe
from frappe import _

def execute(filters=None):
    columns = get_columns()
    data = get_gym_member(filters)
    labels = []
    values = []
    for k in data:
        labels.append(k['test_type'])
        values.append(k['count'])
        chart = {
        "type": "bar",
        "data": {
			"labels": labels,
			"datasets": [
				    {"values": values},	
        	],
        },
    }
    return columns, data, "calories report", chart
  
   

def get_columns():
    columns = [
        {
            'fieldname': 'test_type',
            'label': 'Test Type',
            'fieldtype': 'Data'
           
        },
        {
            'fieldname': 'count',
            'label': 'Count',
            'fieldtype': 'Int'
        },
    ]
    return columns

def get_gym_member(filters=None):
    class_counts = {
        "Blood Test": 0,
        "MIR": 0,
        "X-Ray": 0,
        "Diabetes":0
    }

    data1 = frappe.db.get_list("Exam Schedule", fields=["test_type"])
    for exam_schedule in data1:
        test_type = exam_schedule.get("test_type")
        if test_type in class_counts:
            class_counts[test_type] += 1
        else :
            class_counts[test_type] = 1
    data = []
    for test_type, count in class_counts.items():
        data.append({"test_type": test_type, "count": count})

    return data