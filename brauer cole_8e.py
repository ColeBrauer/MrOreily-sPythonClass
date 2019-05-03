# modify the higher or lower program from this section to keep track of how many
# times the user has enetred the wrong number. If it is more than 3 times, at
# the end print "That must have been complicated"


print("Let's play a game! Try to guess my favorite number in under 3 tries!")
import time
count = 1
number = "7"
guess = -1
guess = input("What is my favorite number? ")
while count < 3 and guess.lower() != number: 
    if guess < number:
        print("It's not that small...")
    elif guess > number:
        print("It's not that big...")
    guess = input("Sorry, try again ")
    count = count + 1

if guess.lower() != number:
    print("You are wrong!") 
    print("That must have been complicated...")
    time.sleep(3)
if guess.lower() == number:
    print("Yes! My favorite number is", number + "!")
    time.sleep(3)
    
