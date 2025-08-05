def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n not in cache:
            if n <= 0:
                return 0
            elif n == 1:
                return 1
            else:
                cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
                return cache[n]
        else:
            return cache[n]

    return fibonacci


fib = caching_fibonacci()
print(fib(10))  # має вивести 55
print(fib(15))  # має вивести 610
