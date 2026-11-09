import json
import sys

F_PATH = 'chi_tieu.json'

def nhap_khoan_chi():
    ten_khoan = input('Nhập tên khoản chi tiêu: ')
    while True:
        temp = input("Nhập số tiền của khoản chi: ")
        try:
            temp = int(temp)
        except ValueError:
            print("Bạn phải nhập vào số nguyên! ")
            continue
        else:
            if (temp < 0):
                print("Bạn phải nhập giá là số không âm !")
                continue
            else:
                so_tien = temp
                break
    danh_muc = input("Nhập vào danh mục chi tiêu: ")
    data_python = {
        "ten_khoan":ten_khoan,
        "so_tien":so_tien,
        "danh_muc":danh_muc
    }
    return data_python


try:
    with open(F_PATH, encoding = 'utf-8') as file:
        data = json.load(file)
    if not isinstance(data,list):
        print("Dữ liệu trong file không ở dạng danh sách hợp lệ!")
        sys.exit()
except FileNotFoundError:
    print("File chưa tồn tại , khởi tạo file mới!")
    data = []
except json.JSONDecodeError:
    print("File bị lỗi không thực hiện chương trình!")
    sys.exit()

data_python = nhap_khoan_chi()
data.append(data_python)
with open(F_PATH,'w',encoding = 'utf-8') as f:
    json.dump(data, f, ensure_ascii = False, indent =4)
    print("Đã lưu thành công")
print(json.dumps(data, indent = 4, ensure_ascii= False))
