#1. Tuple một giá trị bất biến
#Tuple giống như list nhưng không thể thay đổi giá trị sau khi tạo. Dùng ngoặc tròn hoặc chỉ cần dấu ,
point = (10, 20)
rgb_color = (255, 128, 0)
info = ("Alex", 25, "New York")
print(point[0])       # 10
print(len(rgb_color))  # 3
# One-element tuple — the comma is required
single_item = (42,)     # Tuple
not_a_tuple = (42)      # int — just grouping parentheses!
print(type(single_item))  # <class 'tuple'>
print(type(not_a_tuple))  # <class 'int'>

#Tuple không thể sửa
point = (10, 20)
# point[0] = 99   # TypeError: 'tuple' does not support item assignment

#2. Basic Unpacking
name,age,city = ("Tùng Dương", 21,"Hà Nội")
print(name)
print(age)
print(city)

a, b = 10, 20
a, b = b, a
print(a, b)   # 20 10
# Use * to collect the rest
scores = (9, 8, 7, 6, 5)
highest, *rest = scores
print(highest)    # 9
print(rest)       # [8, 7, 6, 5]  — list!

first, *middle, last = scores
print(first, middle, last)   # 9 [8, 7, 6] 5