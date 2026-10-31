tong = 0
while True:
    n = input("Nhập số nguyên dương N: ")
    try:
        n = int(n)
    except ValueError:
        print("Bạn phải nhập một số nguyên dương! ")
        continue
    else:
        if (n<=0):
            print("Bạn phải nhập số lớn hơn 0! ")
            continue
        else:
            print("Các số chẵn : ", end = "")
            for i in range(1,n+1,1):
                if (i % 2) == 0:
                    print(f"{i}",end = "  ")
                    tong += i
        print(f"\nTổng các số chẵn đến {n} là: {tong}")
        break
