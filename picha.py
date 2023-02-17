print("Welcome to the Python Pizza!")
size = input("What size pizza do you wan? S/M/L: ")
peperoni = input("Do you want peperoni? Y/N: ")
chedda = input("Do you want chedda'? Y/N: ")

total = 0
if(size == "S"):
    total += 15
    if(peperoni == "Y"):
        total += 2
    if(chedda == "Y"):
        total += 1
elif(size == "M"):
    total += 20
    if(peperoni == "Y"):
        total += 3
    if(chedda == "Y"):
        total += 1
else:
    total += 25
    if(peperoni == "Y"):
        total += 3
    if(chedda == "Y"):
        total +=1
print("Your Total would be $" + str(total))
