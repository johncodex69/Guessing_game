#This demonstrates a guessing game

from random import randint

#Get user name
username = input("What is your name:")
print("Hello there" + username + "!")

#generate a random number
random_number = randint(10, 50)

counter = 0
while counter < 5:
    user_number = eval(input("Enter a number:"))
    counter += 1

    if user_number < random_number:
        print("Your guess is too low.")
    elif user_number > random_number:
        print("Your guess is too high.")
    elif user_number == random_number:
        break
     
if user_number == random_number:
    print("YOU WIN.")
else:
    print("Game Over! The correct number is")
    print(random_number)