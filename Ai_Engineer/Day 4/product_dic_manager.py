product = {}
product["ma_sp"] = input("Hãy nhập vào mã sản phẩm: ")
product["ten_sp"] = input("Hãy nhập tên sản phẩm:")
while True:
    temp = input("Hãy nhập giá của sản phẩm: ")
    try :
        temp = int(temp)
    except ValueError:
        print("Bạn phải nhập vào số nguyên! ")
        continue
    else:
        if(temp < 0 ):
            print("Giá phải lớn hơn 0")
            continue
        else:
            product["gia"] = temp
            print("Sản phẩm bạn vừa nhập là: ")
            for key, value in product.items():
                print(f"{key}: {value}")
            while True:
                temp = input(f"Bạn hãy nhập giá mới cho sản phẩm {product["ten_sp"]} :")
                try :
                    temp = int(temp)
                except ValueError:
                    print("Bạn phải nhập vào số nguyên! ")
                    continue
                else:
                    if(temp < 0 ):
                        print("Giá phải lớn hơn 0")
                        continue
                    else:
                        product["gia"] = temp
                        print("Sản phẩm sau khi cập nhật là: ")
                        for key, value in product.items():
                            print(f"{key}:{value}")
                        break
            tra_cuu = input("Nhập key bạn muốn tra cứu: ")
            print(f"Key bạn vừa tra cứu có giá trị là: {product.get(tra_cuu,"Không tìm thấy")}")
            del_key = input("Nhập key cần xóa: ")
            xoa = product.pop(del_key,None)
            if (xoa is None):
                print("Không tìm thấy key để xóa! ")
            else:
                print(f"Bạn vừa xóa giá trị {xoa}")
                print("Product sau khi xóa: ")
                for key, value in product.items():
                    print(f"{key}:{value}")
            break
