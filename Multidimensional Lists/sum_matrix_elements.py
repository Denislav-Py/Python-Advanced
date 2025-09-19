# Write a program that reads a matrix from the console and prints:
# * The sum of all numbers in the matrix
# * The matrix itself
# On the first line, you will receive the matrix sizes in the format "{rows}, {columns}".
# On the next rows, you will get elements for each column separated by a comma and a space ", ".

n_rows, n_cols = [int(el) for el in input().split(", ")]

total_sum = 0
matrix = []

for _ in range(n_rows):
    data = [int(el) for el in input().split(", ")]
    total_sum += sum(data)
    matrix.append(data)

print(total_sum)
print(matrix)

# 3, 6
# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0
