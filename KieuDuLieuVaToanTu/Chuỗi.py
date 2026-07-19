#1. Tạo chuỗi
s1 = "single quotes"
s2 = "double quotes"
s3 = ("Một chuỗi"
      "có thể viết nhiều dòng"
      "như thế này")
print(s1)
print(s3)

#2. Nối chuỗi và nhân chuỗi
firts_name = "Do Tung"
last_name = " Duong"
full_name = firts_name +last_name
print(full_name)

dong_ke = "-"*30
print(dong_ke)

#3. Indexing - Truy cập từng ký tự: Mỗi ký tự trong một chuỗi đều có 1 chỉ số index
s = "python"
print(s[0])
print(s[1])
print(s[2])

#4. Cắt chuỗi
print(s[0:3]) #in từ index 0-->3
print(s[3:]) #in từ index 3
print(s[::3])
print(s[::-1])

#Ứng dụng cắt chuỗi
emploee_id = "emp_2022_20"
nam_lam_viec = emploee_id[4:8]
print(nam_lam_viec)

#5. len() - Độ dài chuỗi
name = "Do Tung Duong"
print(len(name))

#6. Một số phương thức thông dụng
name = "Đỗ Tùng DƯƠNG"
print(name.upper()) #ĐỖ TÙNG DƯƠNG
print(name.lower()) #đỗ tùng dương
print(name.capitalize()) #Đỗ tùng dương
print(name.title()) #Đỗ Tùng Dương

#Remove surrounding whitespace
print(name.strip())      # "emma jane WATSON"
print(name.lstrip())     # "emma jane WATSON  "
print(name.rstrip())     # "  emma jane WATSON"

#7. Tìm kiếm và thay thế
address = "Chung cu Osaka, ngo 48 Ngoc Hoi"
print(address.find("Osaka")) #Tìm vị trí của từ "Osaka"
print(address.count(",")) #Tìm số ký tự ","
new_address = address.replace("Ngoc Hoi","Tương Mai")
print(new_address)
# in — membership check
print("District" in address)   #Kiểm tra xem có cái district trong address không?

#8. Split() và join() - Tách / ghép chuỗi
text = "Hoàng Mai, Hai Bà Trưng, Cầu Giấy"
city = text.split(",")
print(city)

#9. Chuỗi là bất biến không thể thay đổi được
s = "hello"
s = "H" +s[1:]
print(s)

#