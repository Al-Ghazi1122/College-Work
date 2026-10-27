

Breaking it down







Feedback section / Bulls Section

Actually a change of plans. I shall show this section in the end

compare the input to the values [] with their indexes / spot in the list.
IF userInput[0] == secret_Digit[0]
THEN PRINT ("1 Bull) XXX
etc etc etc




Make like dice 1 deice 2 etc for each number 
Ten compiled list of thingy together. 
THen compare and INCREMENT EACH bull value.

After all the checking, increment guess as well in an IF Statement 
IF bull <= 4 THEN += guesses.

When bull == 4 then move onto the next stage

Feedback V2 section / Guesses Displaying section

PRINT("It took you about...")
PRINT(guesses + "amount of guesses to guess it right!")

IF guesses >= 3 
THEN PRINT ("You have achieved KING status!")

ELIF guesses <=6 and >= 9
PRINT ("You have achieved mid status")

ELSE 
print ("You have achieved amateur status")

Maybe ask play again 
Maybe save their score and stuff etc.