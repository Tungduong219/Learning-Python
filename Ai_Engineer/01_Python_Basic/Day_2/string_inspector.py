while True:
    string = input("Nhập vào một chuỗi: ")
    if (len(string) <2 ):
        print("Chuỗi bạn nhập vào phải có ít nhất 2 kí tự! ")
        continue
    else:
        print(f"Ký tự đầu: {string[0]}")
        print(f"Ký tự cuối: {string[-1]}")
        print(f"Ký tự ở giữa: {string[1:-1]}")
        print(f"Chuỗi cuối cùng là: {"J"+string[1:]}")
        print(f"Chuỗi gốc: {string}")
        break