import json

def calc_avg_score(students):
    result = []
    for student in students:
        avg_score = round(sum(student["scores"]) / len(student["scores"]), 2)
        result.append({"name":student["name"],"avg_score":avg_score})
    return sorted(result, key=lambda x:x["avg_score"], reverse=True)

print(calc_avg_score([
    {"name": "Alex", "scores": [8, 7, 9]},
    {"name": "Brian", "scores": [9, 8, 8]},
    {"name": "Hung", "scores": [6, 7, 7]},
]))


