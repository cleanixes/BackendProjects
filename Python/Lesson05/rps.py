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
print("You chose " + str(choice) + ".")
print("Python chose " + str(computer) + ".")
print("")

if choice == 1 and computer == 3:
    print("You win!")
elif choice == 2 and computer == 1:
    print("You win!")
elif choice == 3 and computer == 2:
    print("You win!")
elif choice == computer:
    print("You Tie!")
else:
    print("python wins")