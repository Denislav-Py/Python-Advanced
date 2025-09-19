# Write a program that finds the sum of all numbers in a matrix's primary diagonal (runs from top left to bottom right).
# On the first line, you will receive an integer N – the size of a square matrix.
# The next N lines hold the values for each column - N numbers, separated by a single space.

n_rows = n_cols = int(input())

matrix = []

for _ in range(n_rows):
    data = [int(el) for el in input().split()]
    matrix.append(data)


total = 0

for x in range(n_rows):
    for y in range(n_cols):
        if x == y:
            total += matrix[x][y]

print(total)

# 3
# 11 2 4
# 4 5 6
# 10 8 -12



