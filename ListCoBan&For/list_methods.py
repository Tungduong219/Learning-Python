# Khởi tạo một List
from operator import index
from time import process_time_ns

hoa_qua = ["apple","orange","banana","peach"]
#1. Thêm phần tử vào list
#- Thêm 1 phần tử vào cuối danh sách
hoa_qua.append("grape")
print(hoa_qua)

#- Thêm 1 phần tử vào vị trí bất kỳ
hoa_qua.insert(3,"durian")
print(hoa_qua)

#-Nối 1 list khác vào list hiện tại
hoa_qua1 = ["melon","mango"]
hoa_qua.extend(hoa_qua1)
print(hoa_qua)

print(f"-"*50)
#2. Xóa theo giá trị
#- Xóa theo giá trị
hoa_qua.insert(0,"mango")
print(hoa_qua)
hoa_qua.remove("mango")
print(hoa_qua)

# ---- Xóa theo Index---------
hoa_qua.pop(3)
print(hoa_qua)

#----- Xóa phần tử cuối cùng Pop không cần index nhưng có trả về giống như gọi học sinh đứng ra khỏi hàng------------------
hoa_qua.pop()
print(hoa_qua)

#--------- Xóa theo chỉ số dùng số bằng del nhưng là xóa vĩnh viến không có giá trị trả về
del hoa_qua[0]# Xóa phần tử vị trí 1
print(hoa_qua)

#3, Sắp xếp và đảo ngược list
# - Sắp xếp
hoa_qua.sort()
print(hoa_qua)
#Sắp xép truce tiếp
hoa_qua.sort() #Tăng dần
hoa_qua.sort(reverse=True) #Giảm dần
#-SortedList: Trả về 1 list mơới đã sắp xếp không thay dđổi List cũ
sorted(hoa_qua)

#-Đảo ngược
list.reverse(hoa_qua) #Đảo ngược các phần tử trực tiếp trên list gốc
hoa_qua[::-1] #Tạo ra list mới đảo ngược , giữ nguyên list gốc



#4. Tìm kiếm và thống kê
hoa_qua.index("banana") #Trả về index của từ khóa đầu tiên
hoa_qua.count("banana") #Trả về số lần xuất hiện của apple



#5. Các hàm số học tích hơp
number = [1,2,3,4,5,6,7]
print(len(number))
sum(number)
print(sum(number))
print(max(number))
print(min(number))
print(f"AVG: {sum(number)/len(number):.2f}")
