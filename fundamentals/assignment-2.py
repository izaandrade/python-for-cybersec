#Using what we know so far do the following:
#Have a variable with a number between 1 and 20 for the user to guess. (you can research random package if you are feeling frisky).
#Using a loop, ask your user for a number between 1 and 20 (with exception handling in case they enter a string).
#Check user input against the number you have stored.
#When they get it correctly show a success message and end the program.

#BONUS
#If you are feeling extra confident:
#Track how many times the user has guessed.
#Limit the number of guesses and end the program after the user has guessed too many times.
#Display how many guesses the user took to get the correct answer.

import random

number = random.randint(1, 5)  # Gera um número inteiro entre 1 e 5
count = 0
max_attempts = 5

while count < max_attempts:
    try:
        guessing = int(input('Guess the  number>> '))
    except:
        print('Please type a number...')
        continue    
    if guessing == number:
        print("Good job!")
        break
    else:
        print("Try again")
        count += 1

if count == max_attempts: 
    print("End of attemps")
    print(f"The correct number was {number}")
