#Matching Pairs Game

desiredBoard = [ [0],[3],
                 [1],[1],
                 [2],[0],
                 [3],[2],]

list1 = [[0],[1],[2],[3]]
list2 = [[3],[1],[0],[2]]

coverBoard = [[0],[0],
              [1],[2],
              [2],[2],
              [3],[3]]

checkFunc = True

while checkFunc != False:
    # userInput = int(input("Pick a row and a column for your first card"))
    coverBoard [cardArow] = int(input("Pick a row for your first card"))
    coverBoard[cardAcol] = int(input("Pick a column for your first card")) 
    coverBoard[cardArow][cardAcol] = desiredBoard
    print(coverBoard[cardArow][cardAcol])
    if cardArow == [[0]]:
        if cardAcol == [[3]]:
            print("First card matched")
        
        if coverBoard == desiredBoard:
            print ("Finished!") 
            checkFunc = True
        else:
            print ("Not yet")
            checkFunc = False


            print(coverBoard[list1][list2])
            print("First Card UNLOCKED!")

            
    elif userInput == [[1],[1],]:
        print("Second Card MATCHED!")
    elif userInput == [[2],[0],]:
        print("Third Card MATCHED!")
    elif userInput == [[3],[2],]:
        print("Fourth Card MATCHED!")
    else:
        print("Incorrect Card, go again")



