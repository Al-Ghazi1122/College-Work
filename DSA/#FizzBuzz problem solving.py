#FizzBuzz problem solving

for x in range(1,100): # This should be 1,101 not 100. 
    if x // 3:
        print("Fizz")
    elif x // 5:
        print("Buzz")
    elif x // 3 and x // 5: # This should come first because of the logical sequence of it. 
        print("FizzBuzz")
    else:
        print("Error 404")
        