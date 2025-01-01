def factorial(n):
    result = 1
    while n > 1:
        result = n * result
        n -= 1
    return result


def factorial_recursion(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursion(n - 1)

print(factorial_recursion(200))