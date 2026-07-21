#1. Tham số mặc định
def greet(name,greeting = "Hello"):
    print(f"{greeting} {name}")

greet("Alex")
greet("Alex", "hi")
#Tức là ở trên là 1 tham số, tham số đó có thể đổi khi truyền tham số mới vào
#quy tắc: Có giá trị mặc định phải đứng trước không có giá trị mặc định
# Correct
def create_user(name, age, city="Hanoi"):
    return {"name": name, "age": age, "city": city}

# Wrong — SyntaxError
# def create_user(city="Hanoi", name, age):
#     pass

#2. Đối số theo tên Keywords Agument
def studentinfo(full_name, class_name, apartment, avg_score):
    print(f"full name: {full_name} - class name: {class_name} - apartment: {apartment} - avg score: {avg_score}")

studentinfo("Alex", "Hanoi","Thanh Xuan",6.5)
# By name (keyword) — any order works
studentinfo(avg_score=8.5, full_name="Alex", apartment="IT", class_name="K20A")

#3. *args — Nhận số lượng đối số tùy ý
def sum_all(*args):
    print(f"Numbers: {args}")    # args is a tuple
    print(f"Count: {len(args)}")
    return sum(args)

print(sum_all(1, 2, 3))         # 6
print(sum_all(10, 20, 30, 40))  # 100
print(sum_all(5))               # 5

#Kết hợp tham số bình thường với *args:
def score_avg(full_name, *scores):
    """Compute a student's average score."""
    if len(scores) == 0:
        return f"{full_name}: No scores yet"
    avg = sum(scores) / len(scores)
    return f"{full_name}: Avg = {round(avg, 2)}"

print(score_avg("Alex", 8, 7, 9))
# Alex: Avg = 8.0

print(score_avg("Brian", 6, 7, 8, 9, 10))
# Brian: Avg = 8.0

#4. Unpacking list/tuple vào hàm
def add_three(a, b, c):
    return a + b + c

nums = [10, 20, 30]
print(add_three(*nums))   # 60  — same as add_three(10, 20, 30)

scores = (8, 7, 9)
print(add_three(*scores))      # 24


