opened = ["[", "(", "{"]
closed = ["]", ")", "}"]


def check_matching_parenthesis(string_to_check):
    stack = []
    for i in string_to_check:
        if i in opened:
            stack.append(i)
        elif i in closed:
            current = closed.index(i)
            if (len(stack) > 0) and (opened[current] == stack[len(stack) - 1]):
                stack.pop()
            else:
                return "Not matching"
    if len(stack) == 0:
        return "Matching"
    else:
        return "Not Matching"


check_string = "({[{[]}]})"

print(check_matching_parenthesis(check_string))

check_string = "{{[(]]}"

print(check_matching_parenthesis(check_string))
