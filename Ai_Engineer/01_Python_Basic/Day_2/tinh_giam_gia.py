while True:
    so_tien = input("Nhập số tiền khách mua hàng: ")
    try:
        so_tien = int(so_tien)
    except ValueError:
        print("Số tiền bạn nhập chưa hợp lệ!")
        continue
    else:
        if (so_tien <= 0):
            print("Bạn phải nhập số tiền dương!")
            continue
        else:
            print("Bạn đã nhập số tiền hợp lệ!")
            break
while True:
    vip = input("Nhập trạng thai vip của khác hàng (co hoặc khong): ")
    if (vip =="co" or vip =="khong"):
        print("Nhập vip hợp lệ!")
        break
    else: 
        print("Bạn nhập VIP không hợp lệ!")
        continue
while True:
    uu_dai = input("Nhập trạng thái ưu đãi (co hoặc khong): ")
    if (uu_dai =="co" or uu_dai =="khong"):
        print("Nhập trạng thái ưu đãi hợp lệ hợp lệ!")
        break
    else: 
        print("Bạn nhập trạng thái ưu đãi không hợp lệ!")
        continue
bol = uu_dai == "co"
print(f"Tổng cần thanh toán: {so_tien} ")
if ((so_tien >= 500000 or vip == "co") and not(bol)):
    print("Đủ điều kiện sử dụng mã giảm giá!")
    tien_giam = so_tien // 10
    con_lai = so_tien - tien_giam
    print(f"Số tiền đã giảm: {tien_giam}")
    print(f"Số tiền phải thanh toán: {con_lai}")
else: 
    print("Bạn chưa đủ điều kiện sự dụng giảm giá!")
    print("Số tiền giảm giá: 0")
    print(f"Số tiền phải thanh toán cuối cùng {so_tien}")