#This demonstrates a guessing game

from random import randint

#Get user name
username = input("What is your name:")
print("Hello there" + username + "!")

#generate a random number
number = randint(10, 50)

counter = 0
while counter < 5:

#get user number
    user_number = eval(input("Enter a number:"))


#using a while loop
#check if user input is equal to generated number
