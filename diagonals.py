# Using a nested list comprehension, write a program that reads rows of a square matrix and its elements, 
# separated by a comma and a space ", ". You should find the matrix's diagonals, print them, and their sum in the format:
# "Primary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_primary}
# Secondary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_secondary}".


n = int(input())

matrix = []

for _ in range(n):
    data = [int(num) for num in input().split(", ")]
    matrix.append(data)

primary_sum = []
secondary_sum = []

for i in range(n):
    primary_sum.append(matrix[i][i])

for i in range(n):
    secondary_sum.append(matrix[i][-1-i])

print(f"Primary diagonal: {', '.join(str(x) for x in primary_sum)}. Sum: {sum(primary_sum)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_sum)}. Sum: {sum(secondary_sum)}")
