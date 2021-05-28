def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


def fibonacci(n):
    result = []
    a, b = 0, 1

    while b < n:
        result.append(b)
        a, b = b, a + b
    return result


# print(factorial(5)) # 5x4x3x2x1 = 120
# print(fibonacci(1000))
