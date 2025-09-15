# Write a program that reads a sequence of N usernames from the console and maintains a collection of only the unique ones.
# On the first line, you will receive an integer N.
# On the following N lines, you will receive the usernames. Print the collection on the console.

number_of_usernames = int(input())

unique_usernames = set()

for _ in range(number_of_usernames):
    user = input()
    unique_usernames.add(user)

for user in unique_usernames:
    print(user)
