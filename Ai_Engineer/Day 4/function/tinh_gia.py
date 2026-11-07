def nhap_gia_lieu(x):
    while True:
        temp = input(f"Hãy nhập vào một số nguyên cho {x}: ")
        try:
            temp = int(temp)
        except ValueError:
            print("Bạn phải nhập vào một số nguyên!")
            continue
        else:
            if (temp < 0 ):
                print("Bạn phải nhập vào số dương!")
                continue
            else:
                a = temp
                break
    return a

def tinh_thanh_tien(gia, so_luong, giam_gia = 0):
    if(giam_gia >= 0 and giam_gia<=100):
        return gia*so_luong*(1 - (giam_gia/100 ))
    else: 
        print("Bạn nhập giảm giám không hợp lệ, tính theo giảm giá mặc định")
        return gia*so_luong

def hien_thi_hoa_don(ten_sp, don_gia,so_luong,thanh_tien):
    print(f"Tên sản phẩm: {ten_sp}")
    print(f"Số lượng: {so_luong}")
    print(f"Đơn giá: {don_gia}")
    print(f"Thành tiền: {thanh_tien}")

def main():
    ten_sp = input("Nhập tên sản phẩm: ")
    gia = nhap_gia_lieu("giá")
    so_luong = nhap_gia_lieu("số lượng")
    tien = tinh_thanh_tien(gia, so_luong)
    hien_thi_hoa_don(ten_sp, gia,so_luong, tien)
    print("\nÁp dụng giảm giá: ")
    tien1 = tinh_thanh_tien(gia,so_luong, giam_gia= 110)
    hien_thi_hoa_don(ten_sp, gia,so_luong, tien1)

if __name__ =='__main__':
    main()