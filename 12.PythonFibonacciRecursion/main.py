def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n < 0:
        return 'ValueError: Value too small.'
    else:
        return fibonacci(n-1) + fibonacci(n-2)

list1 = [fibonacci(num) for num in range(10)]
print(list1)
