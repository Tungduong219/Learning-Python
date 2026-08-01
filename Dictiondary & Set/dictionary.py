from itertools import count

from ListNangCao_Tuple.ListConprehension import words

student = {
    "name" : "Đỗ Tùng Dương",
    "class": "2310A04",
    "age" : 22,
    "score" : 8
}

#Emty dict
emty = {}
emty2 = dict()

# Tạo từ list of tuple
pairs = [("a",1),("b",2),("c",3),("d",4),("e",5),("f",6)]
d = dict(pairs)
print(d)
print(type(d))

#2. Truy cập và cập nhật
print(student["name"])
print(student["age"])

#3. Cập nhật dict
student["age"] = 23
print(student)

#4. Add new key
student["ngu"] = "yes"
print(student)

print(student.get("phone"))           # None
print(student.get("phone", "N/A"))   # N/A (default value)

#5. Xóa phần tử
del student["ngu"]
print(student)

#6. Xóa nhưng trả về giá trị
age = student.pop("age")
print(age)
print(student)

#7. Trả về tất cả các cây
print(list(student.keys()))
print(list(student.values()))

#8.Unpack
for key, value in student.items():
    print(f"{key}: {value}")

#9. Set default - Lấy hoặc tạo mới
count ={}
words = ["python","programming","programming","programming","sql","sql"]
for word in words:
    count.setdefault(word,0)
    count[word] += 1

print(count)

#10. Update - Gộp dictionary
info = {"full_name":"Alex",
        "age":22}
extra = {"email":"dotungduong2194@gmail.com", "age": 23} # Có thể ghi đè thông tin

info.update(extra)
print(info)

#11. Kiểm tra case có tồn tại không
student = {"full_name": "Alex", "age": 22}

print("full_name" in student)       # True
print("email" in student)        # False
print("email" not in student)    # True

#12. Đếm từ - Ứng dụng
sentences = "Anh cha yeu em, anh cha thuong em, doi"
words = sentences.split()
tan_suat = {}
for word in words:
    tan_suat[word] = tan_suat.get(word, 0) + 1

for word, count in sorted(tan_suat.items()):
    print(f"{word}: {count}")
