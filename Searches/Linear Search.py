#Learning Linear Search at Home

#Quite simple, just goes on by one - Theory

#Example code

def linearSearch(arraylist, target):
    n = len(arraylist) #size of list
    for i in range(0,n): # Till the very end
        if arraylist[i] == target:
            return i #returns the index of i or the value at the current index of i
        return False #could also write return -1 but this makes more sense to me. This is for when its not in the list so exits the for loop and etc.
    
#Lets test this function of binary search now later.
#Could've written this above the function too.

arrayList = [3,4,1,7] #Your array list
target = 1 #required target

result = linearSearch(arrayList, target) #calling the function

if result != False: #or -1
    print("Value", target, "found at index", result)
else: 
    print("Value", target, "not found")

    

