A = int(input('Enter A:'))
B = int(input('Enter B:'))


def swap():
    global A, B
    A, B = B, A
    return True


print(f"Before Swap\nA = {A}\nB = {B}\n")
swap()
print(f"After Swap\nA = {A}\nB = {B}\n")
