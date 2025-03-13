
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n/2+1) + 1):
        if n % i == 0:
            return False
    return True


numbers = (10, 3, 5, 8, 13, 17, 20, 23, 30)

prime_numbers = tuple(num for num in numbers if is_prime(num))

print("Prime numbers in the tuple:", prime_numbers)