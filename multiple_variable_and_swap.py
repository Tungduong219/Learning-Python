#1. Gán nhiều biến cùng lúc

name,age,avg_score = "Dương",24,6.87
print(name,age,avg_score)

#2. Gán cùng giá trị cho nhiều biến
x=y=z=1
print(x)
print(y)
print(z)

#3. Hoán đổi vị trí trong Python
a = 10
b = 20
a,b = b,a #Biểu thức hoán dổi swap
print(f"Giá trị của a sau hoán đổi là: {a}")
print(f"Giá trị của b sau hoán đổi là: {b}")

#4. Hoán đổi nhiều biến
c = 11
d = 22
e = 33
c,d,e = e,d,c
print(c,d,e)

#5. Xóa biến với del - Dùng để xóa biến và giải phòng bộ nhớ ngầm
del a
#hữu ích khi bạn muốn 1 biến không tồn tại sau khi dùng

#6. Unpacking từ list hoặc tuple
fruits = ["apple","banana","cherry"]
x,y,z = fruits
print(x)
print(y)
print(z)

avg_score = (2.3,4.3,5.67)
a,b,c = avg_score
print(a)
print(b)
print(c)

#7. Kiểm tra biến có tồn tại không
try:
    print(a)
except NameError:
    print("The variable does not exist!")