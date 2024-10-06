def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        for i in range(2, int(result)):
            if i == 1:
                continue
            if int(result) % i == 0:
                is_primes = False
                break
            else:
                is_primes = True
        if is_primes:
            print('Простое')
        else:
            print('Составное')
        return result
    return wrapper

@is_prime
def sum_three(*args):
    result = sum(args)
    return result

result = sum_three(2, 3, 6)
print(result)

# result = sum_three(3, 4, 7)
# print(result)