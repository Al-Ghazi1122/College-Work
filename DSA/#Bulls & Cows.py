#Bulls & Cows
#Creator - Muhammad Umar Mahmood 
#2441649

#Importing Modules
import random

#Global Variables
playerName = "x"
guesses = 0
bullValue = 0
cowValue = 0
guesses = 0
secret_Digits_Compiled = "x"

#Section 1 - Game Introduction
print("---------------------------------------------------------------------------------------")
print("🐂 Bulls and 🐄 Cows...")
print("---------------------------------------------------------------------------------------")
print("The best game, the ultimate game")
print("---------------------------------------------------------------------------------------")

#Player Input
playerName = str(input())
print("The following are the game instructions," + playerName)
print("---------------------------------------------------------------------------------------")

#Game Instruction / Segment 1
print("1 - The computer will generate a secret 4 digit number")
print("2 - The computer will NOT display this number and you have to guess this!")
print("BUT HOW DO I KNOW IF I AM GUESSING THE RIGHT NUMBER?! ," + "said somebody")
print("This is where Bulls and Cows come in")
(".......................................................................................")
print("Bulls🐂 - This indicates that you placed a right numbre in the right spot")
print("After each input you will get amount of bulls that were present in your input.")
print("For example, if 1 bull = only one CORRECT number was placed in the CORRECT SPOT. IF two 🐂🐂 = 2 CORRECT Numbers + CORRECT SPOT.")
print(".......................................................................................")
print("Cows - This indicates that you had a correct NUMBER but placed it in the incorrect spot.")
print("After each input you will get amount of cows 🐄 that were present in your input.")
print("Now Cowboy! Ride the 🐂 Bulls and  🐄 cows and guess the number! OR aka until you get all dem four bulls!")

# Secret Digit Subroutine
def secret_Digit():
    secret_Digit1 = random.randint(0,9)([[]]) #Using List/2D Arrays data structure.
    secret_Digit2 = random.randint(0,9)([[]]) # With random function with a single digit limit of 0-9 (10)
    secret_Digit3 = random.randint(0,9)([[]])
    secret_Digit4 = random.randint(0,9)([[]])
    secret_Digits_Compiled = ({secret_Digit1},{secret_Digit2},{secret_Digit3},{secret_Digit4})
    print(secret_Digits_Compiled)
# Main Loop
while bullValue != 4:
# Input Sub-Routine
    checkInput = False
    while checkInput == False:
        userInput = int(input("Enter your guess of FOUR digit number now!!!")) #Only Integer Input Check
 #       if userInput == "": #If input left blank CHECK
  #          print("Sorry I don't understand your blank statements, try again")
        if type(userInput) != int:
            print("Invalid Datatype, only numbers run here")
 #       elif userInput > 4:
 #           print("Only four digits needed sir...")
 #       elif userInput < 4:
#            print("Need at least four digits to proceed")
        else:
 #           userInput = 4
            checkInput = True
    
    #Feedback Section
    print("Processing results...")

    #Bulls Section

    #Digit 1 Check
    for i in bullValue == 4: #For loop for bullValue Check but only till the count goes up to 4 for that would mean the player has guessed the word correctly
        if userInput[0] == secret_Digits_Compiled[0]:
            bullValue += 1
    #Digit 2 Check
        elif userInput[1] == secret_Digits_Compiled[1]:
            bullValue += 1
    #Digit 3 Check
        elif userInput[2] == secret_Digits_Compiled[2]:
            bullValue += 1
    #Digit 4 Check
        elif userInput[3] == secret_Digits_Compiled[3]:
            bullValue += 1
            print(bullValue)
    
        #Cows Section
        #Digit 1 Check
            if userInput[0] == secret_Digits_Compiled[1]:
                cowValue += 1
            elif userInput[0] == secret_Digits_Compiled[2]:
                cowValue += 1
            elif userInput[0] == secret_Digits_Compiled[3]:
                cowValue += 1
        #Digit 2 Check
            if userInput[1] == secret_Digits_Compiled[0]:
                cowValue += 1
            elif userInput[1] == secret_Digits_Compiled[2]:
                cowValue += 1
            elif userInput[1] == secret_Digits_Compiled[3]:
                cowValue += 1
        #Digit 3 Check
            if userInput[2] == secret_Digits_Compiled[0]:
                cowValue += 1
            elif userInput[2] == secret_Digits_Compiled[1]:
                cowValue += 1
            elif userInput[2] == secret_Digits_Compiled[3]:
                cowValue += 1
        #Digit 4 Check
            if userInput[3] == secret_Digits_Compiled[0]:
                cowValue += 1
            elif userInput[3] == secret_Digits_Compiled[1]:
                cowValue += 1
            elif userInput[3] == secret_Digits_Compiled[2]:
                cowValue += 1
                print(cowValue)
        #Guesses
            if bullValue > 4:
                guesses += 1

# If bullValue == 4
    break

#Number of Guesses OUTPUT
print("It took you about...")
print(guesses + "amount(s) of guesses to crack the secret digit!")
print("The secret digit number was, " + secret_Digits_Compiled)
if guesses >= 3:
    print("You have achived KING DETECTIVE status")
elif guesses <= 6 and guesses >= 9:
    print("You have achieved mid Detective status")
else:
    print("You have achieved junky detect status")

#END GAME OUTPUTS
print ("You've met your fate partner, whatever status that may be")
print ("Better luck next time.")
print("END OF")
print("----------------------------------------------------------------")