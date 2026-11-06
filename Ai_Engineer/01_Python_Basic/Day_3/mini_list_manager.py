list = []
while True:
    print("===== MINI LIST MANAGER =====")
    print("1. Xem danh sách")
    print("2. Thêm số nguyên")
    print("3. Chèn vào vị trí tùy chọn")
    print("4. Xóa theo giá trị")
    print("5. Xóa theo vị trí")
    print("0. Thoát chương trình")
    choice = input("Hãy nhập lựa chọn của bạn: ")
    if choice == "1":
        if len(list)==0:
            print("Danh sách rỗng!")
        else:
            print("Danh sách hiện tại của bạn: ")
            for i in range(len(list)):
                print(f"index: {i} - {list[i]}")
    elif choice == "2":
        while True:
            a = input("Nhập giá trị phần tử muốn thêm vào danh sách: ")
            try:
                a = int(a)
            except ValueError:
                print("Bạn chỉ được nhập số nguyên!")
                continue
            else:
                list.append(a)
                print(f"Đã thêm {a} vào danh sách")
                break
    elif choice == "3":
        while True:
            chen = input("Nhập giá trị muốn chèn vào:")
            try:
                chen = int(chen)
            except ValueError:
                print("Bạn phải nhập vào giá trị nguyên!")
                continue

            while True:
                vi_tri = input("Nhập vị trí bạn muốn chèn: ")
                try:
                    vi_tri = int(vi_tri)
                except ValueError:
                    print("Bạn phải nhập vào 1 số nguyên!")
                    continue
                else: 
                    if (vi_tri in range (len(list)+1)):
                        list.insert(vi_tri,chen)
                        print("Đã chèn xong")
                        break
                    else: 
                        print("Vị trí chèn vào không hợp lê!")
                        continue
            break
    elif choice == "4":
        while True:
            xoa = input("Hãy nhập giá trị số nguyên cần xóa: ")
            try:
                xoa = int(xoa)
            except ValueError:
                print("Bạn nhập giá trị không hợp lệ! ")
                continue
            else:
                if xoa in list:
                    list.remove(xoa)
                    print("Đã xóa theo giá trị thành công!")
                    break
                else: 
                    print("Giá trị bạn nhập không có trong danh sách!")
                    break
    elif choice == "5":
        if(len(list)>0):
            while True: 
                vi_tri_xoa = input("Nhập index cần xóa: ")
                try:
                    vi_tri_xoa = int(vi_tri_xoa)
                except ValueError:
                    print("Bạn phải nhập vào 1 số nguyên!")
                    continue
                else:
                    if (vi_tri_xoa < 0 ):
                        print("Không nhận giá trị index âm!")
                        continue

                    else:
                        if (vi_tri_xoa not in range(len(list))):
                            print("Vị trí index không hợp lệ!")
                            break
                        else: 
                            value_del = list.pop(vi_tri_xoa)
                            print(f"Bạn vừa xóa giá trị: {value_del}")
                            break
        else:
            print("Danh sách rỗng")

    elif choice == "0":
        print("Chào bạn!")
        break
    else: 
        print("Lựa chọn của bạn không hợp lệ!")
