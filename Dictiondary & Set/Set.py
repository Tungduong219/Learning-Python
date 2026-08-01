#1. Tạo set
colour = {"Blue","Red","Yellow","Blue"}
print(colour)
print(len(colour))

figure = [1,2,3,4,5,6,5,4,3,2,1]
num_set = set(figure)
print(sorted(num_set))

#set rỗng
emty = {}# Đây là dict rỗng không phải set rỗng
emty_set = set() #Đây mới là emty set
print(type(emty))
print(type(emty_set))

#2. Thêm và xóa phần tử
#add - thêm phần tử
ngon_ngu = {"Python","SQL"}
ngon_ngu.add("Java")
ngon_ngu.add("Python")
print(sorted(ngon_ngu))

