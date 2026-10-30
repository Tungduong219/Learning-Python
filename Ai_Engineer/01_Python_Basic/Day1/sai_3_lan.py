count = 0
while count < 3:
    diem = input("Nhập điểm của bạn: ")
    try: 
        diem = int(diem)
    except ValueError:
        print("Giá trị bạn nhập vào không hợp lê!")
        count +=1
        continue
    else:
        if(diem < 0 or diem > 10):
            print("Điểm bạn nhập phải trong khoang 0 đến 10")
            count +=1
            continue
        else:
            print(f"Điểm của bạn nhập là:{diem}")
            break
else: print("Bạn đã hết số lượt nhập!")
