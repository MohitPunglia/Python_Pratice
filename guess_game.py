# Generate a random number and ask user to guess that number, return the attempt user took to guess the correct number

import random

jackpot=random.randint(1,100)

count=1
 
guess=int(input("Guess the number :"))

while jackpot!= guess :
    if guess < jackpot : 
        print('Guess higher')

    else:
        print('Guess lower')
    
    
    guess=int(input("Guess the number :"))
    count +=1

print('Correct Guess!!')
print('Your correct guess was ', count, 'attempts')


 
