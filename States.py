# Imports Random Function that operates on random events
import random

# Takes a dictionary from a separate python file to stop cheaters from reading the program while the terminal is running
from States_CheatSheet import capital_dic

# Turns all the keys of the dictionary into a list
keys = list(capital_dic.keys())

# Sets all scoring values to 0, also implements the variable x that controls the y loop
x = 0
win = 0
loss = 0

# While loop that runs 10 times, making input appear 10 times
while x < 10:
    # Takes a random word for the Keys list
    ran_word = random.choice(keys)

    # Takes user input, asking the user for the capitol of the randomly selected states
    enter = input(f"What is the capitol of {ran_word}? ")

    # Runs the input through 2 if statements, wrong or right
    if enter == capital_dic[ran_word]:
        # If someone gets the score right it prints the following
        print("nice one")

        # This also adds 1 to x so the while loop has 1 less loop on it
        x += 1

        # Keeps score if how many the user gets right
        win += 1

        # Gets rid of the state so they don't have to enter a capitol of a state more than once
        keys.pop(keys.index(ran_word))

    elif enter != capital_dic[ran_word]:
        print("wrong")
        x += 1

        # Same thing for if someone gets it wrong, just adds to a separate variable
        loss += 1
        keys.pop(keys.index(ran_word))

# Prints the final results after the loop concludes
print(f"You won {win} times!!!")
print(f"You lost {loss} times!!!")