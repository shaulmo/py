print("Welcome to the Tilt-O-Wheel Ride")
age = int(input("What is your age? number (e.g 31): "))
height = float(input("What is your height? meter (e.g 1.8): "))

if(age < 12):
    bill = 5
    print("Ticket is $5")
elif(age <= 18):
    bill = 7
    print("Ticket is $7")
elif(age >= 45 or age <= 55):
    bill = 0
    print("You get a free ride!")
else:
    bill = 12
    print("Ticket is $12")

photo = input("Do you want a photo taken? Y/N: ")
if(photo == "Y"):
    bill += 3
print(f"Total price is ${bill}")
