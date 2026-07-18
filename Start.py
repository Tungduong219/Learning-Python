x = 5
y = "John"
print(x,",",y)
x = str(5)
print(type(x))
z = float(8)
print(type(z))
print(type(y))
A=3
a= 3
print(A+a)
#Tên biến
ten_cua_ban = "Đỗ Tùng Dương"
ten_cua_ban2 = "Đỗ Tùng Dương"
yourName = "Tùng Dương" #Camel Case
YourName = "Trần Huy Khánh" #Pascal Case
your_name = "Đỗ Trung Kiên" #snake Case

#Gán giá trị cho nhiều biến
duongName,khanhName,namName = "Đỗ Tùng Dương", "Trần Huy Khánh","Vũ Văn Nam"
#Gán nhiều biến 1 giá trị
duongdName = khanhhName = nammName = "Đỗ Tùng Dương"
#Unpacking giải nén
fruits = ["apple", "banana", "cherry"]
x,y,z = fruits
print(x)

#Biến đầu ra:
x = "Python is awesome"
print(x)
x = "python"
b = "is"
c = "awesome"
d = 5
print(x,b,c)
print(x+b+c)
print(x,d)

#Biến toàn cục --> Trong hàm ưu tiên sử dụng biến trong hàm hơn Globle Variables.
x= "awesome"
def myfunc():
    global x
    x = "dep zai"
    print("Duong is "+x)

myfunc()
print("Duong rat "+x)

#Các kiểu dữ liệu
x = ("apple", "banana", "cherry")
print(type(x))