# Stacks and Queues # Data Structures

#Variable Declaration

pointer = -1 #Not 0 
CONSTANT = 5 #Max size of stack
stack = [None] * CONSTANT # Cant have nothing in it for some reason (list of everything ready for stack)

# isempty, isfull, pop, push, peek, traversal

def isFull():
    return pointer == CONSTANT - 1 #If only using push() then use this statement in push function

def push(item):
    global pointer # Any changes made to pointer will only be kept in here
    if isFull():
        print("Stack Overflow!")
    else:
        pointer += 1
        stack[pointer] = item #Mutable Objects notice the lists
        print(item, "Added to stack ") 
    return
pass

def isEmpty():
    return pointer == - 1  
def pop(item):
    global pointer 
    if isEmpty():
        print("Stack Empty!")
    else:
        print(stack[pointer], "Removed from stack")
        stack[pointer] = None 
        pointer -= 1

    return

def peek():
    return print (stack[pointer])

def traversal():
    for index in range(pointer, -1, -1):
        print(stack[pointer])
    

print(stack)
print("END OF STACKY STACK")




