import random

number_to_guess = random.randint(1,100)

while True:
   try:
      user_input = int(input("Guess the number between 1 and 100: "))

      if user_input < number_to_guess:
         print("Too Low!")
      elif user_input > number_to_guess:
         print("Too high!")
      else:
         print("Congratulations! You guessed the right number.")
         break
   except ValueError():
      print("Please enter a valid number")
