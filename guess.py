import random
from mimetypes import guess_all_extensions

guessestaken=0

print("what is your name")
MyName=input()

number=random.randint(1,20)

print('Well, ' + MyName + ', I am thinking of a number between 1 and 20.')

while (guessestaken<5):
    print('Take a guess , dude')
    guess=input()
    guess=int(guess)


    guessestaken=guessestaken+1
    guesstaken2=guessestaken-1

    if(guess<number):
        print('your guess is too low , make a good guess dude')

    if(guess<number):
        print("you only have this number of guesses left = " , guesstaken2)

    if(guess>number):
     print('your guess is too high , dont be too high !! man')

     if (guess != number):
         print("you only have this number of guess left =  ", guesstaken2)

    if(guess==number):
     break

if(guess==number):
    guessestaken=str(guessestaken)
    print('Good job, ' + MyName + '! You guessed my number in ' + guessestaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)




