#Learning Linked List by myself / AT HOME NOTES

LinkedList = [ [ "A", 1] , 
             ["B", 3] ] # Index of lists and items as its a doubly linked list.

start = 1
index = start #Not fully understanding this ATM, but maybe its so that the list doesnt stop after going to an item with the index as "None" ??? Summat like that, Ill have to reconfirm
while index is not None: 
    print(LinkedList)[index][0] #[index] for 1 (the list at 1), and [0] for the items at list 1 which is B. If it was [1] then perhaps the output would've been 3
    index = LinkedList[index][1] # Something for traversal but honestly dont understand this at all. I can only see that the index's value (head pointer) would change?