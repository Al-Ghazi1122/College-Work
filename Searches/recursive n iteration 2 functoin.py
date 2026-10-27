#Function to make which returns the sum of all non negative integers
# Basically saying that whatever input you get you write numbers till the input itself and then it adds em

def sumFunc(n):
    total = 1
    for x in range(n + 1): # not 1 at the start as it will add one to it at teh nd
        total+= x
        return total #Iterative version for this code
    

def sumFuncRecur(n):
    if n == 0:
        return 0
    else:
        return n + sumFuncRecur(n - 1)
    

print(sumFuncRecur(3))