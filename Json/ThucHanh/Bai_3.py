import json
raw_json = '''
[
  {
    "student_id": "SV01",
    "name": "Đỗ Tùng Dương",
    "scores": {"python": 9.0, "ai_base": 8.5},
    "city": "Hà Nội"
  },
  {
    "student_id": "SV02",
    "name": "Nguyễn Văn A",
    "scores": {"python": 6.5, "ai_base": 7.0},
    "city": "Đà Nẵng"
  },
  {
    "student_id": "SV03",
    "name": "Trần Thị B",
    "scores": {"python": 8.0, "ai_base": 9.5},
    "city": "Hà Nội"
  }
]
'''
python_raw_json = json.loads(raw_json)
print(python_raw_json)
for student in python_raw_json:
    gpa = (student["scores"]["python"]+student["scores"]["ai_base"])/2.0
    student["gpa"] = gpa
print(python_raw_json)

exellent_student = []
for student in python_raw_json:
    exellent_student.append({
        "name": student["name"],
        "gpa": student["gpa"]
    })

file_name = "exellent_student.json"
with open(file_name, "w",encoding="utf-8") as f:
    json.dump(exellent_student, f,indent=4,ensure_ascii=False)