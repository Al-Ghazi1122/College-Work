#Name - Muhammad Umar Mahmmood
#Assignment Number - 1 Dice Game

#Importing Modules
import random


#Global Variables
playerName = str(input("Enter your gamertag, challenger! :"))
# highscorer = "" 
totalPoints = 0 # **** NOT SURE YET ****
highscore = totalPoints
playAgain = True
char = " "

                
##############

print("********")
print("Dice Game, The Ultimate Game")
print("The current highscore is " )
# print("By" + highscorer) 
print("Are you up for the mighty challenge, " + playerName + "?")

#Rules & Instructions
#Rules based on 3 Values
print("The Rules for scoring are as follows:-")
print(".....................................")
print("- If all 3 dice have the same value = +25 points")
print("- If all 3 dice values are in sequence = +20 points")
print("- If all 3 dice have an even value = +15 points")
print("- If all 3 dice values are odd = +15 points")
print("- If all 3 dice values are same = +15 points")
print("- If 2 of the dice have the same value = +10 points") #Only rule that adds points with 2 values
print("                                                   ")
print("Failing to meet one of these will mean you have died, and the game will finish.")

#MainLoop
while playAgain == True:
    print("Please press spacebar to get your dice numbers")
    diceNumbers = input()
 
#Dice Randomization Process / Sub-Program 
    diceRandomization = False
    if diceNumbers == char:
        diceRandomization = True
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        dice3 = random.randint(1,6)
        print (f"You got: {dice1}, {dice2}, {dice3}")
    else: 
        diceRandomization = False
        print("Invalid Input, please press space to roll the dice")

  #  response = input(" ").upper() 
