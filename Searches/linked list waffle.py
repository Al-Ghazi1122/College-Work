# Linked Lists

listy = [["A", 40], ["B", 20] , ["C", 10]]
lar = listy[0]
sma = listy[0]
print(lar, "is lar \n", sma , "is sma")

for things in listy: #1st way of getting a value from the list. Gets the list within the list
    if lar[1] < things[1]:
        lar = things

for thing in range(ken(listy)) #2nd way of returning a value from the list
    if listy[things][1] > sma[1]
    sma = lar[1]

print(f" {lar[0]} is the largest with {lar[1]}")