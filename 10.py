import random 
secretNumber = random.randint(1,20)
print("I am thinking  of a number between 1 and 20")

# Ask the players to guess 6 times
for guessesTaken in range(1,7):
    print("Take a guess")
    guess = int(input())

    if guess < secretNumber:
        print("You guess is too low.")
    elif guess > secretNumber:
        print("Your guess is too high")
    else: 
     break # this condition is the correct guess

if guess == secretNumber:
     print('Good job! You guessed my number in ' + str(guessesTaken) + 'guesses!')
else: 
     print('Nope. The number i was thinking of was ' + str(secretNumber))
























while True: 
    print("Take a guess")
    numberGuess = int(input())
    numOfAttempts = (0)

    if numberGuess <= 15:
        numOfAttempts = numOfAttempts + 1
        print("Your guess is too low.")
    elif numberGuess >= 17:
        print("Your guess is too high.")
        numOfAttempts = numOfAttempts + 1
    elif numberGuess == 16:  
            numOfAttempts = numOfAttempts + 1
            print("Good job! You guessed my number in " + str(numOfAttempts) + " guesses!")
            exit()