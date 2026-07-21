#1. Định nghĩa hàm
def hello():
    print("Xin chào mọi người")
    print("Chào every one")

hello()
hello()

#2. Hàm có tham số
def Hello(name):
    print(f"Hello {name}")

Hello("Dep zai co gi sai?")
Hello("Thong minh lam thang ngu a")

def add(x, y):
    return x + y

print(add(1, 2))

#3. Lệnh return trả về giá trị thay vì chỉ in ra màn hình - khi gặp return hàm trả về giá trị ngay, các câu lệnh sau return không chạy
def tinhDienTich(a,b):
    area = a * b
    return area
print(tinhDienTich(2,3))

#4. Có thể tra về nhiều giá trị
def ham1(nums):
    tong = sum(nums)
    tring_binh = sum(nums) // len(nums)
    lon_nhat = min(nums)
    nho_nhat = max(nums)
    return tong,tring_binh,lon_nhat,nho_nhat

score = [1,2,3,4,5]
tong,tring_binh,lon_nhat,nho_nhat = ham1(score)
print(tong,tring_binh,min,max)

#5. docString - Tài liệu cho hàm
def calc_bmi(weight, height):
    """Calculate the BMI index.

    Args:
        weight: Weight in kg
        height: Height in meters

    Returns:
        BMI rounded to 2 decimal places
    """
    bmi = weight / (height ** 2)
    return round(bmi, 2)

print(calc_bmi(70, 1.75))   # 22.86
print(calc_bmi(55, 1.60))   # 21.48

#6. Hàm không có return
def calc_bmi(weight, height):
    """Calculate the BMI index.

    Args:
        weight: Weight in kg
        height: Height in meters

    Returns:
        BMI rounded to 2 decimal places
    """
    bmi = weight / (height ** 2)
    return round(bmi, 2)

print(calc_bmi(70, 1.75))   # 22.86
print(calc_bmi(55, 1.60))   # 21.48

"""
Tên hàm dùng snake_case: calc_area, count_words, classify_student
Mỗi hàm nên làm một việc duy nhất — ngắn gọn, rõ ràng
Luôn viết docstring cho hàm quan trọng
return dừng hàm ngay lập tức — code sau return không chạy
Hàm không có return trả về None
Đặt tên tham số có ý nghĩa: weight thay vì x
"""