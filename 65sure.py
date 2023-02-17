print("Welcome to the Treasure Island. Your mission is to find the treasure.")
leftOrRight = input("Left or Right? L/R: ")
if(leftOrRight == "L"):
    swimOrWait = input("Swim or Wait? S/W: ")
    if(swimOrWait == "W"):
        whichDoor = input("Which door? Red, Yellow or Blue? R/B/Y: ")
        if(whichDoor == "R" or whichDoor == "B"):
            print("Game over.")
        elif(whichDoor == "Y"):
            print("You Win!")
        else:
            print("Wrong answer")
    else:
        print("Game is Over.")
else:
    print("Game Over")
