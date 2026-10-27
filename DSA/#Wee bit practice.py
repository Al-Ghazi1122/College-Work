#Wee bit practice

#sentence, characters As String 
sentence= "Hello World!" 

# print(sentence[2:]) #Cut up the first two, get everything else

# print(sentence[:2]) #Cut up everything, get me the first two.

# print(sentence[:-2]) #Cut up the last two

# print(sentence[-2:]) #Cut up everything, get me the last two

# print(sentence[2:-2]) #Cut up the first two, cut up the last two = 

# print(sentence[2:5])  #Cut from the first two, cut from the last 5.

# print(sentence:2) 
# ----- ------------- - String slicing

city1= input("PLease entre city 1")
inputupper = city1.upper()
city2 = input("City 2")
cityUpper2 = city2.upper()
# lencity1 = len(inputupper) 
# lencity2 = len(cityUpper2)

#4 characters
citychar4 = inputupper[:4]
citychar4c2 = cityUpper2[:4]

# last1 = inputupper + lencity1
# last2 = cityUpper2 + lencity2

print(citychar4 + "-" + citychar4c2)


#Didnt use len(), neither find.word() 