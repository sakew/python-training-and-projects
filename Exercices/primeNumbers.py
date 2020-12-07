def is_prime(n):
    for x in range(2, int(n / 2 + 1)):
        if not n % x:
            return False
    return True


def primes_to(n):
    for x in range(2, n):
        if is_prime(x):
            print(x)
