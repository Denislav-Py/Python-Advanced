# Write a program that reads a matrix from the console and prints the sum for each column on separate lines.
# On the first line, you will get matrix sizes in the format "{rows}, {columns}".
# On the next rows, you will get elements for each column separated with a single space.

n_rows, n_columns = [int(el) for el in input().split(", ")]

matrix = []

for _ in range(n_rows):
    data = [int(el) for el in input().split()]
    matrix.append(data)

for y in range(n_columns):
    current_sum = 0
    for x in range(n_rows):
        current_sum += matrix[x][y]
    print(current_sum)

# 3, 6
# 7 1 3 3 2 1
# 1 3 9 8 5 6
# 4 6 7 9 1 0
