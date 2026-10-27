#Learning Searches from Alex
    
list = [9, 8, 10, 2, 12, 7, 1, 20]

#Linear search

'''
target = 8

found = False
for i in list:
    if target == i:
        found = True

print(found)
'''
'''
Validation

def validation(low,high):
    valid=False
    while not valid:
        try:
            opt = int(input("Enter an option: "))
            if opt >= low and opt <= high:
                return opt
            else:
                print("Not in range")
        except ValueError:
            print("Incorrect value type")
            '''

print("1. Option 1")
print("2. Option 2")
print("3. Exit")
low=1 # This is the same as
user_option = validation(1,3) # This. 

# print("6. Option 1")
# print("7. Option 2")
# print("8. Exit")
# user_option = validation(6,8) 

# Thanks to Alex Nezu I have finally understood functions, why they are needed,  the importance of "parameters" and that this way you can call it all the time without rewriting teh code.
