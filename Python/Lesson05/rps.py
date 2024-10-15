import random
import sys
#value = input('Please enter a value:\n')

#print(value)

print("")
choiceP = input("Enter... \n1 for Rock, \n2 for Paper, \n3 for Scissors:\n\n")
choice = int(choiceP)

if choice < 1 | choice > 3:
    sys.exit("invalid")

computerChoice = random.choice("123")
computer = int(computerChoice)

print("")
print("You chose " + choice + ".")
print("Python chose " + computer + ".")
print("")