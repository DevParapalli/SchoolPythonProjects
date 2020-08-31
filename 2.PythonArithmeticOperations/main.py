import my_math
addition = my_math.add
subtraction = my_math.subtract
multiplication = my_math.multiply
division = my_math.divide


def main():
    alpha = int(input("Enter value of A: "))
    beta = int(input("Enter Value of B: "))
    print("Values Entered: A --> {}".format(alpha))
    print("                B --> {}".format(beta))
    print("Addition :      {}".format(addition(alpha, beta)))
    print("Subtraction :   {}".format(subtraction(alpha, beta)))
    print("Multiplication: {}".format(multiplication(alpha, beta)))
    if beta == 0 :
        print("Division by Zero Not Supported")
    else:
        print("Division :      {}".format(division(alpha, beta)))

if __name__ == "__main__":
    main()