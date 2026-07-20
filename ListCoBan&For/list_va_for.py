#1. Tạo list
score = [7,7.5,8,8.5,9,9.5]
#List of Strings
student_name = ["Duong","Khanh","Nam","Kien","Vu"]
#Mixed list
mixed = ["Duong",25,8.5, True]
#emty_list
emty_list = []
print(score)
print(student_name)
print(mixed)
print(len(score))

#2. Indexing - Truy cập phần tử
fruits = ["apple","banana","orange"]
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[-1])
print(fruits[-2])
print(fruits[-3])

fruits[1]="durian"
print(fruits)

#3. Vòng lặp for - Duyệt từng phần tử
for name in student_name:
    print(f"Hello {name}")

total = 0;
for s in score:
    total += s
print(total)
print(f"Total: {total}")
print (f"Average: {total/len(score)}")

#4. range() tạo dãy số
for s in range(6):
    print(s, end=" ")
print()

for s in range(2,8):
    print(s, end=" ")
print()
# range(start, stop, step) — with a step
for s in range(0,20,2):
    print(s, end="  ")
print()

# Count down
for s in range(10,0,-1):
    print(s, end="  ")
print()

#5. Kết hợp for, range và list
for s in range(len(student_name)):
    print(f"{s+1}.{student_name[s]}")

#6. enumerate() — Vừa lấy index vừa lấy giá trị
subjects = ["maths", "physics", "chemistry","English"]
for subject,idx in enumerate(subjects,start=1):
    print(f"{subject}. {idx}")