from collections import defaultdict

from multiple_variable_and_swap import avg_score

squares = {x: x**2 for x in range(1,6)}
print(squares)

origanal = {"a":1, "b":2,"c":3}
inverted = {v: k for k , v in origanal.items()}
print(inverted)
top_organal = {v:k for k,v in origanal.items() if v>1}
print(top_organal)

scores_student = {"Tung Duong" : 6.5, "Khanh":8.5, "Nam":9.5, "Vu":4.5 , "Kien":7.8}
top_students = {name:s for name,s in scores_student.items() if s>8}
print(top_students)
down_students = {name:s for name,s in scores_student.items() if s<8}
print(down_students)

#Tạo dict từ 2 list bằng zip
item = ["Computer", "Mouse","Laptop","Keyboard"]
price = [200,500,500,500]
#Cách 1: dict + zip
score_table = dict(zip(item, price))
print(score_table)
#Cách 2: dict comprehension + zip
score_table = {i:p for i,p in zip(item,price)}
print(score_table)

#3. Nested dict - Dict lồng nhau
#Tạo và truy cập, hiện
students = {
    "Tung Duong":{
    "age":22,
    "scores":{"Toan":10,"Anh":5,"Van":7},
    "class":"A12A03"
},
    "Huy Khanh":{
        "age":40,
        "scores": {"Toan":4,"Anh":10,"Van":8},
        "clases":"A1293L"
    }
}
print(students["Huy Khanh"]["scores"])

#Cập nhật
students["Tung Duong"]["scores"] = {"Toan":10,"Anh":9,"Van":9.5}
print(students["Tung Duong"]["scores"])

#duyêt vòng lặp
students = {
    "Alex": {"math": 8, "literature": 7, "english": 9},
    "Brian": {"math": 9, "literature": 8, "english": 8},
    "David": {"math": 6, "literature": 7, "english": 7},
    "Emma":  {}
}

for name,scores in students.items():
    if not scores:
        print(f"Học sinh {name} chưa có điểm số nào")
        continue
    avg_score = round(sum(scores.values())/len(scores),2)
    print(f"The average score of {name} is: {avg_score}")

#4. Dict of List
#Khởi tạo dữ liệu đầu vào
students_list = [
    ("Tùng Dương","2310A04"),
    ("Huy Khánh","2310A05"),
    ("Văn Nam","2310A06"),
    ("Khánh Toàn","2432A33")
]

class_groups = defaultdict(list)
for name, clases in students_list:
    class_groups[clases].append(name)

for cls, name_list in sorted(class_groups.items()):
    print(f"{cls}: {name_list}")


orders = [
    {"product": "Laptop", "price": 25_000_000, "quantity": 2},
    {"product": "Mouse", "price": 500_000, "quantity": 10},
    {"product": "Laptop", "price": 25_000_000, "quantity": 1},
    {"product": "Keyboard", "price": 1_200_000, "quantity": 5},
]

thongke = {}
for o in orders:
    p = o["product"]
    amount = o["price"] * o["quantity"]
    thongke[p] = thongke.get(p, 0) + amount

for p, rev in sorted(thongke.items(), key=lambda x: x[1], reverse=True):
    print(f"{p}: {rev:,} VND")