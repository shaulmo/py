print("Welcome to the Rollercoaster ride!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5 #print("Child tickets are $5.")
    elif age <= 18:
        bill = 7 #print("Youth tickets are $7.")
    else:
        bill = 12 #print("Adult tickets are $12.")
    photo = input("Do you want your photo taken? Y/N ")
    if photo == "Y":
        bill += 3
    if photo == "N":
        bill
else:
    print("Sorry, you need to meet the requirements.")

print(f"That would be ${bill} kind sir")
