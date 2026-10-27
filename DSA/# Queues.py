# Queues

rear = -1
front = 6
MAX = 7
queue = [None] *MAX

# isEmpty, isFull, Enqueue, Dequeue, Peek, Traversal

def isFull():
    return (front == rear + 1) or (front == 0 and rear == MAX -1)

def enqueue(item):
    global front
    if isFull():
        print("Cannot Enqueue any furhter, its full!")
    else:
        rear += 1
        queue[rear] = item
        print(item , "Added Dude!")
        if isEmpty():
            rear -= 1
            rear = 0
    else:
        rear == MAX
        rear = 0

def isEmpty():
    return rear == front-1 
    rear == 0 and front == MAX-1

def dequeue():
    global rear
    global front # both
    if isEmpty():
        print("Queue Empty")
    # else:
    #     queue[front] = None
    #     if front == rear:
    #         front = -1
    #         rear = -1
    #     else:
    #         front +1 = 1
    #         if front == MAX
    #         front = 0
    #Sirs COde!
        front -= 1
        queue[front] = item
        print(item, "First guy outta the line")
    else:
        front == MAX
        front = 0

def peek():
    return print(queue[front][rear])

def traversal():
    while index in range(MAX, -1,-1):
        print(queue[front][rear])

# Sirs traversal
def travsersal():
    index = front
    while True :
        print(queue[index])
        if index == back:
            break
        index +1 = 1
        if index == MAX
        index = 0