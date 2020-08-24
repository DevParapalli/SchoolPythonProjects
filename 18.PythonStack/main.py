Stack = [9, 8, 7, 6, 5, 4, 3, 2, 1]

def remove():
    """
    Removes Top Element
    """
    global Stack
    Stack = Stack[1:]

def add(item):
    global Stack # makes sure we are modifying the global Stack variable.
    new_stack = []
    new_stack.append(item)
    for element in Stack:
        new_stack.append(element)
    Stack = new_stack

print(Stack)
remove()
print(Stack)
add(10)
print(Stack)


