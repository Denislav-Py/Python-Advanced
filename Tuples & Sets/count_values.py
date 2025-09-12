# You will be given numbers separated by a space.
# Write a program that prints the number of occurrences of each number in the format "{number} - {count} times".
# The number must be formatted to the first decimal point.

nums = ([float(el) for el in input().split()])

data = {}

for el in nums:
    if el not in data:
        data[el] = nums.count(el)


for number, count in data.items():
    print(f"{number} - {count} times")
