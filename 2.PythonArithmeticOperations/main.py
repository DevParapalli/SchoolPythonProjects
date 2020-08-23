def add(a,b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def main():
    alpha = int(input("Enter value of A: "))
    beta = int(input("Enter Value of B: "))
    print("Values Entered: A --> {}".format(alpha))
    print("                B --> {}".format(beta))
    print("Addition :      {}".format(add(alpha, beta)))
    print("Subtraction :   {}".format(subtract(alpha, beta)))
    print("Multiplication: {}".format(multiply(alpha, beta)))
    if beta == 0 :
        print("Division by Zero Not Supported")
    else:
        print("Division :      {}".format(divide(alpha, beta)))

if __name__ == "__main__":
    main()