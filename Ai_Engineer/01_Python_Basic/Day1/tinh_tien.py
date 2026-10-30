ten_sp = input("Nhập tên sản phẩm: ")
while True:
    so_luong = input("Nhập số lượng : ")
    try:
        so_luong = int(so_luong)
    except ValueError:
        print("Số lượng phải là một số nguyên!")
    else:
        if (so_luong < 0):
            print("Số lượng không hợp lệ!")
            continue
        else:
            don_gia = int(input("Nhập đơn giá: "))
            thanh_tien = so_luong * don_gia
            print(f"Tên sản phẩm: {ten_sp}")
            print(f"Số lượng: {so_luong}")
            print(f"Đơn giá: {don_gia}")
            print(f"Thành tiền: {thanh_tien}")
            break
