import random

doors = ["door1", "door2", "door3"]

# Put a car in a door
car = random.choice(doors)

# Get decision1 from user
decision1 = input("Choose a door: ")

# Reveal a door
while True:
    reveal = random.choice(doors)
    if reveal != car and reveal != decision1:
        break
print(f"Behnd {reveal}, there is a goat.")

# Get decision2 from user
print(f"Your first choice: {decision1}")
decision2 = input("Choose a door again: ")

# Reveal all door
if car == "door1":
    print("Door1: Car, Door2: Goat, Door3: Goat")
elif car == "door2":
    print("Door1: Goat, Door2: Car, Door3: Goat")
else:
    print("Door1: Goat, Door2: Goat, Door3: Car")

# Result
print(f"Your first choice: {decision1}" , f"Your second choice: {decision2}", sep='\n')
if decision2 == car:
    print("You won the car! :)")
else:
    print("You lost the car! :(")
