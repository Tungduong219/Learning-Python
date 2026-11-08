ten_khoan = input("Nhập tên khoản chi tiêu: ")
while True:
    temp = input("Hãy nhập số tiền cần chi: ")
    try :
        temp = int(temp)
    except ValueError:
        print("Bạn phải nhập vào vào 1 số dương")
        continue
    else:
        if (temp < 0 ):
            print("Bạn phải nhập vào số dương! ")
            continue
        else:
            so_tien = temp
            with open("chi_tieu.txt","a",encoding = "utf-8") as file:
                file.write(f"{ten_khoan}  {so_tien}\n")
                print("Đã ghi file thành công")

            with open("chi_tieu.txt","r",encoding = "utf-8") as file:
                s = file.read()
                print(s)
            break
