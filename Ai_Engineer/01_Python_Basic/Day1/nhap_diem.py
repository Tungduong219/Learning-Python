while True:
    diem = input("Nhập điểm của bạn: ")
    try: 
        diem = int(diem)
    except ValueError:
        print("Điểm phải là một số nguyên!")
        continue
    else:
        if(diem < 0 or diem > 10):
            print("Điểm không hợp lệ! Vui lòng nhập điểm từ 0 đến 10.")
            continue
        else: 
            print(f"Điểm của bạn nhập hợp lê, diem ban vua nhap la:{diem}")
            break