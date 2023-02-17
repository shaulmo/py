print("Welcome to the matching Calc")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

firstLower = name1.lower()
secondLower = name2.lower()

firstCountT = firstLower.count("t")
firstCountR = firstLower.count("r")
firstCountU = firstLower.count("u")
firstCountE = firstLower.count("e")
secondCountT = secondLower.count("t")
secondCountR = secondLower.count("r")
secondCountU = secondLower.count("u")
secondCountE = secondLower.count("e")
firstResult = firstCountT + firstCountR + firstCountU + firstCountE + secondCountT + secondCountR + secondCountU + secondCountE

oneCountL = firstLower.count("l")
oneCountO = firstLower.count("o")
oneCountV = firstLower.count("v")
oneCountE = firstLower.count("e")
twoCountL = secondLower.count("l")
twoCountO = secondLower.count("o")
twoCountV = secondLower.count("v")
twoCountE = secondLower.count("e")
secondResult = oneCountL + oneCountO + oneCountV + oneCountE + twoCountL + twoCountO + twoCountV + twoCountE

print(str(firstResult) + str(secondResult))
