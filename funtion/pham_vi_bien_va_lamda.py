#1. Phạm vi biến
#- Biến local được tạo ra trong hàm à hủy khi kết thúc hàm
def area():
    length = 10
    width = 20
    return length * width

area = area()
print(area)

# Global Scope - Biến toàn cục
school_name = "Xom Data Academy"   # global variable

def print_school():
    print(f"School: {school_name}")  # Reading a global variable — OK

print_school()   # School: Xom Data Academy
print(school_name)   # Xom Data Academy
# Muốn đổi biến cục bộ thành toàn cục thì sử dụng global
call_count = 0

def increment_counter():
    global call_count
    call_count += 1
    print(f"Call count: {call_count}")

increment_counter()   # Call count: 1
increment_counter()   # Call count: 2
increment_counter()   # Call count: 3

#2. Quy tắc LEGB
x = "global"  # G — Global


def outer_func():
    x = "enclosing"  # E — Enclosing

    def inner_func():
        x = "local"  # L — Local
        print(x)  # Finds L first → "local"

    inner_func()
    print(x)  # x in enclosing → "enclosing"


outer_func()
print(x)  # x in global → "global"

#3. Lambda - Hàm ẩn danh là cách viết hàm một dòng ngắn gọn, không cần đặt tên:
# Regular function
def square(x):
    return x ** 2

# Equivalent lambda
square_lambda = lambda x: x ** 2

print(square(5))         # 25
print(square_lambda(5))  # 25

#Lambda nhiều tham số :
add = lambda a, b: a + b
print(add(3, 5))   # 8

compute_bmi = lambda weight, height: round(weight / (height ** 2), 2)
print(compute_bmi(70, 1.75))   # 22.86


#Lambda kết hợp sorted - Ứng dụng phổ biến nhất
students = [
    {"name": "Alex", "score": 8.5},
    {"name": "Brian", "score": 9.0},
    {"name": "Charlie", "score": 7.5},
]

# Sort by score, ascending
by_score = sorted(students, key=lambda s: s["score"])
for s in by_score:
    print(f"{s['name']}: {s['score']}")
# Charlie: 7.5
# Alex: 8.5
# Brian: 9.0

# Sort by name
by_name = sorted(students, key=lambda s: s["name"])
for s in by_name:
    print(s["name"])
# Alex, Brian, Charlie


#Lambda với map và filter :
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)   # [2, 4, 6, 8, 10]

# Square everything
squares = list(map(lambda x: x ** 2, numbers))
print(squares)   # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Combine: square the odd numbers
result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, numbers)))
print(result)   # [1, 9, 25, 49, 81]




