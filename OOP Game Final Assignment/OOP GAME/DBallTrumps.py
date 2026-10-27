# Custom Dragon Ball Z Themed Top Trumps Game
# Muhammad Umar Mahmood 2441649

import random
import time

# ----------------------
    # OOP
    # Card Class

def classLoop():
    class Card:
        def __init__(self, name, strength, speed, stamina):  # attributes & encapsulation
            self.name = name
            self.strength = strength
            self.speed = speed
            self.stamina = stamina

        def displayStats(self):
            print(f"{self.name}: Strength {self.strength}, Speed {self.speed}, Stamina {self.stamina}")

    class CharacterTings:
        def __init__(self, name):
            self.name = name
            self.hand = []

        def hasCards(self):
            return len(self.hand) > 0

    class Player(CharacterTings):
        def chooseAttribute(self, card):
            print("Your card:")
            card.displayStats()
            print("Pick an attribute (strength / speed / stamina):")
            attribute = input().lower()
            return attribute

    class Computer(CharacterTings):  #computer choosing the best attribute
        def chooseAttribute(self, card):
            if card.strength >= card.speed and card.strength >= card.stamina:
                bestAttr = "strength"
            elif card.speed >= card.stamina:
                bestAttr = "speed"
            else:
                bestAttr = "strength"
            print(f"Computer chooses {bestAttr}!")
            return bestAttr
            
    #Deck
        deck = [
            Card("Goku", 95, 90, 85),
            Card("Vegeta", 92, 88, 80),
            Card("Gohan", 89, 85, 82),
            Card("Frieza", 85, 87, 75),
            Card("Piccolo", 80, 78, 85),
            Card("Trunks", 88, 86, 78),
            Card("Cell", 90, 83, 80),
            Card("Majin Buu", 93, 70, 95),
            Card("Krillin", 65, 72, 68),
            Card("Tien", 70, 75, 72)
        ]

        random.shuffle(deck)
        half = len(deck) // 2

        player = Player(username)

        playerHand = deck[:half]
        computerHand = deck[half:]

        comp = Computer("Computer Player")  # Using the Computer class
        compHand = deck[:half]
        
        round_number = 1

#Main Game Logic / Main Game Loop

# ----------------------
# Previous User's Login Data (File Handling)
filename = "userData.txt"
user_data = []  # Empty array, here the user data shall be saved.

file = open(filename, "r")
for line in file:
    line = line.strip()
    usernameNLvl = line.split(",")
    user_data.append(usernameNLvl)
file.close()

# ----------------------
# Game Instructions (User experience focused)
print("************************************")
print("WELCOME TO DRAGON BALL Z TOP TRUMPS! THE ULTIMATE GAME!")
time.sleep(2)
print("The game rules are very simple and are as follows: -")
print("You shall be playing against a computer")
print("You shall get half a deck of cards - same as your opponent.")
print("Whoever goes first is decided purely by LUCK")
print("From this point you must choose the best attribute of ANY of your cards and play to win!")
print("Your chosen card's chosen attribute will be compared against your opponent's and whoever wins... ")
print("gets to collect that card and use it within their deck of cards, ultimately making them stronger.")
print("The winner of the round will also then decide the attribute to be compared for the next round")
print("IF HOWEVER, your card and their card has somehow magically got the exact same power then")
print("that card goes to a POOL round and whoever wins the next round after that shall receive all those cards")
print("UNTIL! A player runs out of cards. At that point the game is declared over and scores are updated on the screen.")
print("Good luck warrior! Show us what you've got! SUPER SAIYAN!")
# A powerful quote
print("....................................")
print("Power comes in response to need, not a desire. You have to create that need - Son Goku")
print("....................................")

# ----------------------
# Game starto!
# Creating new users, validating inputs and welcoming return users
# User experience focused
print("Are you a new player? Press Y for Yes or N for No.")
userType = input().upper()
username = ""
level = 0

if userType == "Y":
    print("Please enter your new username:")
    username = input()
    usernameExists = False  # False flag for if username already exists
    for user in user_data:
        if user[0] == username:
            usernameExists = True
            break
    if usernameExists:
        print("Username already exists! Please restart and try again.")
    elif username == "":
        print("Invalid choice. Please restart the game.")
    else:
        print("New user created at Level 0!")
        file = open(filename, "a")
        file.write(username + "," + str(level) + "\n")  # Datatype conversion
        file.close()
        classLoop()

elif userType == "N":
    print("Enter your existing username:")
    username = input()
    if username == "":
        print("Invalid choice. Please restart the game.")
    else:
        found = False
        for user in user_data:
            if user[0] == username:
                level = int(user[1])
                found = True
        if found:
            print(f"Welcome back {username}! Your current level is {level}.")
            classLoop()
        else:
            print("Username not found! Please restart the game.")
