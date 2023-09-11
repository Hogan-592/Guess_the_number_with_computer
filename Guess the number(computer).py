#This project uses random library that's built in python and ask computer to guess the number we have in mind
import random

#Define a function which we can call upon
def computer_guess(x):
    #set our lower and upper bound
    low = 1
    high = x
    #We need to provide feedback to the computer to see if the number computer guessed is correct or not
    #Give feedback varibale a initial value
    feedback = ''

    #construct a while loop as long as the number computer guessed is not correct
    while feedback != 'c':
        #Fix a bug here for when the lower bound equals to upper bound. /
        #eg: computer gussed 8, then we say it is too low, hence lower bound becomes 8+1 = 9, and then computer guessed 10, we say it is too high, our upper bound would become 10-1=9.
        #So they match, but we want the user to say whether it is correct or not
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low #could also be high cos low = high
        #use lower function to convert everything into lower case
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)? ').lower()
        if feedback == 'h': #if it is too high, then any number higher than this don't need to consider
            high = guess - 1
        elif feedback == 'l': #if it is too low, then any number less than this don't need to consider
            low = guess + 1

    #The following line only executes when the while loop is done
    print(f'Yay, The computer guessed your number,{guess}, correctly!')

#Call the function
computer_guess(1000)
