#Prime number checker

num = 0
checkerndat = False

numInput = int(input("Enter a number g: "))

if num == 0 or num == 1:
    print("not a prime number")

elif num >1:
     for each in range(2,numInput):
          if (num%numInput) == 0:
            checkerndat = True
            break
if checkerndat == True:
    print(numInput, "is not a prime number")
else:
    print(numInput, "is prime number innit")
    
 
