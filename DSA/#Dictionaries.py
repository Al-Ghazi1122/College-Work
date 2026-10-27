#Dictionaries
badger = {"Name" : "Jeff" , "Age" : 3 , "Snout": Pointy }
badgerL = [ "Jeff" , 3 , "Pointy"]
print(badgerL[0])
print(badger["Name"])
chickens = {}
chickens["Name"] = "Bilbo"
chickens["Claws"] = "Scratchy"
chickens["Claws"] = "blunt"
chickens[]
print(chickens)
del chickens["Claws"]
badger = {"Name" : "Jeff" , "Age" : 3 , "Snout": Pointy }

for badKey in badger.keys():
    print(badKey)
for badval in badger.values():
    print(badval)

for badkey, badval in badger.items():
    print(badKey , "Is the key")
    print(badval , "Is the value")

cheeses = {
    "brie" : {"stink value": 66 , "Taste" : "Mild" } , 
    "cheddar" : {"stink value": 34 , "Taste" : "Strong" } , #Brie etc is row, and the values inside it are the values. Like 2D Arrays
    "strings" : {"stink value": 2 , "Taste" : "Mild" }
    }

print(cheeses["cheddar"]["Taste"]) 

countries = {
    "Australia" : {"Capital": "Sydney" , "Population" : 500},
    "Brazil" : {"Capital" : "Brasilia" , "Population" : 600},
    "Canada" : {"Capital" : "Chicago" , "Population" : 400},
    "Denmark" : {"Capital" : "Copenhagen" , "Population" : 200},
    "England" : {"Capital" : "London" , "Population" : 700}
}

print = ("Please input a population size in hundreds, e.g. 100 etc")
input = int(input())

for capital in countries.values() > 200:
    print(countries ["Australia"])
    print(countries ["Brazil"])
    print(countries ["Canada"])
    print(countries ["England"])
