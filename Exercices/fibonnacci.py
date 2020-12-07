def fibonacci(n):
    if n <= 0:
        # this is the first fibonacci number

        print("0 is the first fibonacci number")

    # this is the second fibonacci number
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# or using dynamic programming
array = [0, 1]


def dynamic_fibonacci(n):
    if n <= 0:
        print("nope")
    elif n <= len(array):
        return array[n - 1]
    else:
        sum_of_numbers = dynamic_fibonacci(n - 1) + dynamic_fibonacci(n - 2)
        array.append(sum_of_numbers)
        return sum_of_numbers


# or a recursive method

def recursive_fibonacci(n):
    if n <= 1:
        return n
    else:
        return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


number = 9
for i in range(number):
    print(recursive_fibonacci(i))
