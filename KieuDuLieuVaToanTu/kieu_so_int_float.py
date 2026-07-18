#1. int (số nguyên) không có phần thập phân. Trong python có thể dài vô hạn và không bị tràn
age = 92
maxs = 90_000_090_000_000
print(maxs)

#2.Float là chữ số có phần thập phân
score_avg = 8.5
pi = 3.14159
temperature = -2.7
ratio = 0.75

print(type(score_avg))

#3. Các toán tử trong Python
# Real-world example: computing salary
base_salary = 10_000_000
coefficient = 1.5
bonus = 2_000_000

net_salary = base_salary * coefficient + bonus
print(f"Salary: {net_salary:,.0f} VND")

#4. Thứ tự ưu tiên các toán tử
print(2 + 3 * 4)      # 14 (Nhân chia trước)
print((2 + 3) * 4)    # 20 (Trong ngoặc trước)
print(10 - 3 + 2)     # 9  (Trái ang phải
print(2 ** 3 ** 2)    # 512 (Phải sang trái)

#5. Toán tử rút gọn
score = 10
score += 2    # score = score + 2 → 12
score -= 3    # score = score - 3 → 9
score *= 2    # score = score * 2 → 18
score /= 3    # score = score / 3 → 6.0
score //= 2   # score = score // 2 → 3.0
print(score)  # 3.0

#6. Chuyển đổi kiểu số
#- int() chuyển sang số nguyên, cắt bỏ số thực
print(int(3.9))      # 3  (no rounding!)
print(int(3.1))      # 3
print(int("42"))     # 42 (converts a numeric string)

#- float() convent to float add .0
print(float(5))        # 5.0
print(float("3.14"))   # 3.14


#7. Mộ số hàm có ích
# round() laàm tròn số
print(round(3.14159, 2))
print(round(3.8))
print(round(4.1))

#abs() trị tuyệt đối
print(abs(-5))

#min(),max - Min max
print(max(1,5,3,5,3,7))
print(min(5,3,2,1,1))




