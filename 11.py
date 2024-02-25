print("I am thinking  of a number between 1 and 20")
numOfAttempts = 0

while True: 
    print("Take a guess")
    numberGuess = int(input())

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