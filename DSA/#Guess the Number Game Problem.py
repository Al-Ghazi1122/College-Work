#Guess the Number Game Problem

import random

randomNum = random.randint(1,100)
found = False
numberEntered = 0

while numberEntered >= 1 and numberEntered >= 100 and found == False:
    numberEntered = input("Enter a numbre between 1-100")
    if (int(numberEntered)) == randomNum:
        print("You are SUCCESSFUL!!!!")
    elif (int(numberEntered)) > randomNum:
        print("too high")
    elif (int(numberEntered)) < randomNum:
        print("Too Low")
    else:
        found = True
        print("Error")
