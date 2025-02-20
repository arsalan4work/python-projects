# Snake, water, gun game
# 1 for snake
# -1 for water
# 0 for gun 
import random
computer = random.choice([1, -1, 0])
youstr = input("1 for snake, -1 for water, 0 for gun. Enter your choice: ")
you_dict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}
you = you_dict[youstr]
print(f"You chose {reverseDict[you]} \n Computer choose {reverseDict[computer]}")

if computer == you:
      print("It's a Draw!")
else:
   if computer == -1 and you == 1:
      print("Computer wins")
   elif computer == 1 and you == 0:
         print("Computer wins")
   elif computer == 0 and you == -1:
         print("Computer wins")
   elif computer == 1 and you == -1:
         print("You win")
   elif computer == 0 and you == 1:
         print("You win")
   elif computer == -1 and you == 0:
         print("You win")
   else:
         print("Draw")