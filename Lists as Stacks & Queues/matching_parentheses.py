# You are given an algebraic expression with parentheses. Scan through the string and extract each set of parentheses. Print the result back on the console. 

some_text = input()

stack = []

for i in range(len(some_text)):
    if some_text[i] == "(":
        stack.append(i)
    elif some_text[i] == ")":
        start_index = stack.pop()
        end_index = i + 1
        print(some_text[start_index:end_index])
