Queue = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def remove():
    global Queue
    Queue = Queue[1:]

def add(item):
    global Queue
    Queue.append(item)


print(Queue)
remove()
print(Queue)
add(54)
print(Queue)