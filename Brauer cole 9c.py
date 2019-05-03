# rewrite the high_low.py program from lesson 4c to use a random integer between
# 0 and 00 and the user only gets 6 guesses use the python documentation to
# find an appropriate module and cuntion to do this.
# http://docs.python.org/2/library/

import random
print("Let's play a game! Try to guess my favorite number in under 6 tries!")
number = random.randint(1, 99)
count = 0
guess = int(input("What is my favorite number? "))
while count < 5 and guess != number: 
    if guess < number:
        print("It's not that small...")
    if guess > number:
        print("It's not that big...")
    guess = int(input("Sorry, try again "))
    count = count + 1

if guess != number:
    print("You are wrong!") 
    print("That must have been complicated...")
    print("The number was", number)
if guess == number:
    print("Yes! My favorite number is", number)

    
