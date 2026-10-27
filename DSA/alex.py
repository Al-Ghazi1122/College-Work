#String Slicing
#Uppending
#Prime Numbers and dat
#Dictionaries
#For loop
# Lists
#Reverse Order

#validation
def num_validation(r1,r2):
    valid=False
    while not valid:
        try:
            num=int(input("Enter a number: "))
            if num >= r1 and num <= r2:
                return num
            else:
                print("Not in range")
        except ValueError:
            print("Incorrect data type")

#prime number checker
user_number = num_validation(1,10000)

divisor_list=[]
for each in range(1,user_number):
    if user_number%each == 0:
        divisor_list.append(each)

if len(divisor_list) > 2:
    print("Not prime")
else:
    print("Prime")

#perfect number checker
total=0
for each in range(1,user_number):
    if user_number%each == 0:
        total=total+each

if user_number==total:
    print("Perfect")    
else:
    print("Not perfect")

#appending a dictionary to a list
list=[]

new_entry = {
    'name': 'alex',
    'pass': '123'
}

list.append(new_entry)
print(list)