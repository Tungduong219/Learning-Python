#1. List Comprehension là gì?
#List comprehension là cách viết tạo list mới từ iterable trong một dòng duy nhất. Đây là một trong những tính năng Pythonic nhất, giúp code ngắn dễ đọc.\
# Traditional way: use a loop
squares = []
for x in range(1, 6):
    squares.append(x ** 2)
print(squares)   # [1, 4, 9, 16, 25]

# List comprehension: much more concise!
squares = [x ** 2 for x in range(1, 6)]
print(squares)   # [1, 4, 9, 16, 25



#Thêm điều kiện if
# Filter even numbers from 1-20
evens = [x for x in range(1, 21) if x % 2 == 0]
print(evens)   # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Filter words longer than 4 characters
words = ["Python", "SQL", "Data", "AI", "Machine", "Learning"]
long_words = [w for w in words if len(w) > 4]
print(long_words)    # ['Python', 'Machine', 'Learning']

# Filter numbers divisible by both 3 AND 5
divisible = [x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0]
print(divisible)  # [15, 30, 45, 60, 75, 90]

#if-else trong comprehension
# Label even/odd
numbers = [1, 2, 3, 4, 5]
labels = [f"{x} even" if x % 2 == 0 else f"{x} odd" for x in numbers]
print(labels)
# ['1 odd', '2 even', '3 odd', '4 even', '5 odd']

# Clamp scores: min 0, max 10
score_raw = [-2, 5, 12, 8, -1, 10, 15]
score_clamped = [max(0, min(10, s)) for s in score_raw]
print(score_clamped)   # [0, 5, 10, 8, 0, 10, 10]


# Build multiplication tables for 2-4
times_table = [[f"{i}x{j}={i*j}" for j in range(1, 4)] for i in range(2, 5)]
for row in times_table:
    print(row)
# ['2x1=2', '2x2=4', '2x3=6']
# ['3x1=3', '3x2=6', '3x3=9']
# ['4x1=4', '4x2=8', '4x3=12']

# Flatten a nested list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]
print(flat)   # [1, 2, 3, 4, 5, 6, 7, 8, 9]