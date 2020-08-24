def factorial(num: int):
    if num == 1:
        return 1
    elif num == 0:
        return 1
    elif num < 0:
        return 'NaN'
    else:
        return num * factorial(num - 1)

print(factorial(10))