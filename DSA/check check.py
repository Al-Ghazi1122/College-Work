# for x in range(5): 
#             print("This is how you get code to repeat") 

# # Nicked from teams but in range funciton, the parameter/ the bracket that it has in front of it, it has 5 as a stopping value as it REQUIRED. 
# # the start value is optional, stop value is required and step is also optional

word= "Hello" 
for x in range(1,len(word)+1):  #len(word) on its own would be 5 and +1 = 6 so total is 1 start to 6 stop. 
    print("Letter",x, "is",word[x-1]) # x-1 FIRSTLY should be 1-1 as 1 because it starts from 1 cuz of range not 0. and 1 index would be e but since -1 so its H
 
 # Alright honestly this code is so complicated. 

wordy = "yo"
print(len(wordy[1:1])) # index 1 is 0 so the len of 1 is just 1 letter.
# what is 1:1 doing now. it returns 0 but why..
