import random

doors = ["door1", "door2", "door3"]
chosen = random.choice(doors)

# Put a car in a door
car = random.choice(doors)

# Reveal a door
while True:
    reveal = random.choice(doors)
    if reveal != car and reveal != chosen:
        break

# Get decision2 from user

#Avoiding chosen2 and chosen from being the same
while True:
    chosen2 = random.choice(doors)
    if chosen2 != chosen and chosen2 != reveal:
        break

# Reveal all door
if car == "door1":
    print("Door1: Car, Door2: Goat, Door3: Goat")
elif car == "door2":
    print("Door1: Goat, Door2: Car, Door3: Goat")
else:
    print("Door1: Goat, Door2: Goat, Door3: Car")

# Result
print(f"The first choice: {chosen}" , f"The second choice: {chosen2}", sep='\n')
if chosen2 == car:
    print("The computer won the car! :)")
else:
    print("The computer lost the car! :(")
