
# LinkedList = [ [ "R" , 2 ] ,  #0 - #Index of lists within
#                 ["B" , 4 ] , #1
#                 ["S" , None ] , #2
#                 [None , 0 ] , #3
#                 ["C" , 0] , #4
#                 [None , None ] ] #Linked Lists visualised - Every item has a pointer to go to the next pointer.
#                 #0       #1  === #Index of items within
# #Traversal and Searching = Operations

# start = 1 #Start at B
# index = start #Temp variable, so it doesn't get stuck after the pointer goes to S and None. 
# while index is not None: #Validation check before startin 
#     print(LinkedList[index][0] ) #Notice there are two indexes as there are two lists. 
#     index = LinkedList[index][1] # As Index's pointer changes it keeps going back for traversal.

#     #This was a traversal operation algorithm. Search algo isnt much different from this.

LinkedList = [ [ "R" , 2 ] ,  #0 - #Index of lists within
                ["B" , 4 ] , #1
                ["S" , None ] , #2
                [None , 0 ] , #3
                ["C" , 0] , #4
                [None , None ] ] #Linked Lists visualised - Every item has a pointer to go to the next pointer.
                #0       #1  === #Index of items within
#Traversal and Searching = Operations

searchFor = "C"
found = False

start = 1 #Start at B
index = start #Temp variable, so it doesn't get stuck after the pointer goes to S and None. 
while index is not None and != "C": #Validation check before startin 
    print(LinkedList[index][0] ) #Notice there are two indexes as there are two lists. 
    index = LinkedList[index][1] # As Index's pointer changes it keeps going back for traversal.

    #This was a traversal operation algorithm. Search algo isnt much different from this.