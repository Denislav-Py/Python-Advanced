# Write a program that reads a matrix from the console and finds the 2x2 top-left submatrix with the biggest sum of its values.
# On the first line, you will get matrix sizes in the format "{rows}, {columns}".
# On the next rows, you will get elements for each column, separated with a comma and a space ", ".
# You should print the found submatrix and the sum of its elements, as shown in the examples.

import sys

n_rows, n_cols = [int(el) for el in input().split(", ")]\

matrix = []

for _ in range(n_rows):
    data = [int(el) for el in input().split(", ")]
    matrix.append(data)

max_sum = -sys.maxsize
sub_matrix = []

for x in range(n_rows - 1):
    for y in range(n_cols - 1):
        current_number = matrix[x][y]
        next_number = matrix[x][y + 1]
        below_number = matrix[x + 1][y]
        diagonal_number = matrix[x + 1][y + 1]

        total_sum = current_number + next_number + below_number + diagonal_number
        if total_sum > max_sum:
            max_sum = total_sum
            sub_matrix = [[current_number, next_number], [below_number, diagonal_number]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)

# 3, 6
# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0




