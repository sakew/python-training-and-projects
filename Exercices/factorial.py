
def factorial(n):

    non_recursive_result = 1

    if n == 0:
        return 1
    else:
        for i in range(1, n + 1):
            non_recursive_result = non_recursive_result * i
        return non_recursive_result


number = input("Enter a number: ")


def recursive_factorial(n):

    if n == 0:
        return 1

    return n * recursive_factorial(n-1)


result = recursive_factorial(int(number))

print("The number is: " + number + " and the factorial is: " + str(result))
