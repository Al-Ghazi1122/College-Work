#Traversal Circular Queue / Traversal Linked List

start = 1
free = 2
def traversal(LL, st):
    index = st
    while index is not None:
        print(LL[index][0])
        index = LL[index][1],
traversal(linked_list , start)

def freeTrav(LL , fr):
    index = fr
    while index is not None:
        print(f"Index {index} is free!")