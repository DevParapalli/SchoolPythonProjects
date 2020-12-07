STACK = [64, 128, 32, 81, 69]

def pop():
    """
    Removes Top Element
    """
    global STACK
    STACK = STACK[1:]

def push(item):
    """Removes the 

    Args:
        item ([type]): [description]
    """
    global STACK # makes sure we are modifying the global Stack variable.
    new_stack = []
    new_stack.append(item)
    for element in STACK:
        new_stack.append(element)
    STACK = new_stack

print(STACK)
pop()
print(STACK)
push(10)
print(STACK)


