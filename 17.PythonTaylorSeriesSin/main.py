import numpy as np 
""" Numpy on windows has a error in the current version
"""

factorial = np.math.factorial
real_sin = np.math.sin
pi = np.pi

angle = pi/3
no_of_iter = 20 # keep under 80, otherwise causes OverflowError. 


def taylor_nthterm(x, n):
    sign = (-1) ** n
    numerator = x ** ((2*n) + 1)
    denominator = factorial((2*n) + 1)
    return sign * numerator / denominator


def sin(x, n):
    sin_value = 0
    for i in range(n):
        sin_value = sin_value + taylor_nthterm(x, i)
        print("Current Iteration {}, Value: {}".format(i, sin_value))
    return sin_value

output = f"Sin Calulated: {sin(angle, no_of_iter)}, Sin Actual: {real_sin(angle)}, Error: {real_sin(angle)-sin(angle, no_of_iter)}"

print(output)