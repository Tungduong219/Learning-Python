#1. Slicing nâng cao - cú pháp[start,stop,step]
numbers = [0,1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:7])  # [2, 3, 4, 5, 6]   — from index 2 up to (not including) 7
print(numbers[::2])  # [0, 2, 4, 6, 8]   — step 2 (even indexes)
print(numbers[1::2]) # [1, 3, 5, 7, 9]   — start at 1, step 2 (odd indexes)
print(numbers[::-1])     # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  — reversed
print(numbers[-3:])      # [7, 8, 9]         — last 3 elements
print(numbers[::-3])
#Slicing luôn trả về list mới, không thay đổi list cũ

#2. Gán giá trị qua slicing
#Có thể thay 1 phần của list = slicing
scores = [5,6,7,8,9]
scores[1:3] = [10,10]
print(scores)

# Replace with a list of a different length
scores[1:3] = [20]
print(scores)              # [5, 20, 8, 9]  — the list shrinks
# Insert without removing
scores[2:2] = [99, 100]
print(scores)              # [5, 20, 99, 100, 8, 9]

#3. Nested List — List lồng nhau (List 2D)
grade_table = [
    ["Alex", 8, 7, 9],
    ["Brian", 9, 8, 8],
    ["Charlie", 6, 7, 7],
]
print(grade_table[0])        # ['Alex', 8, 7, 9]  — first row
print(grade_table[0][0])     # 'Alex'             — first student's name
print(grade_table[1][2])     # 8                  — Brian's literature score

for student in grade_table:
    name = student[0]
    average = round(sum(student[1:]) / 3, 2)
    print(f"{name}: average = {average}")

#4. Copy vs Reference — Bẫy nguy hiểm
a = [1, 2, 3]
b = a           # b points to the same list as a
b[0] = 99
print(a)        # [99, 2, 3]  — a changed too!

# Ways to create a copy
c = a[:]         # Slicing creates a new list
d = a.copy()     # The copy() method
e = list(a)      # The list() constructor

c[0] = 777
print(a)    # [99, 2, 3]  — a is not affected

import copy
#Muốn ko đổi dùng ngay deepcopy
matrix = [[1, 2], [3, 4]]
matrix_copy = copy.deepcopy(matrix)
matrix_copy[0][0] = 99
print(matrix)        # [[1, 2], [3, 4]]  — not affected