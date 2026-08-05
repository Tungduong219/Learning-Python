import json
json_str = """
{
    "course_id":"AI901",
    "title" : "Hành trình học AI",
    "is_active":true,
    "students":["Cường","Bình","Minh"],
    "duration_hours": null
}
"""
dict_data = json.loads(json_str)
print(dict_data)
print(type(dict_data))
dict_data["students"].append("Dương")
dict_data["duration_hours"] = 40
print(dict_data)
print("-"*20)
#Chuyển sang kiểu đẹp
format_dict = json.dumps(dict_data,indent=4,ensure_ascii=False,sort_keys=True)
print(format_dict)