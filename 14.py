import random, sys 

wins = 0
losses = 0
ties = 0

while True: 
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    
    print("Hello Player, above this message you shall see your current leaderboard standing.")
    print("Would you like to continue? (Y / N)")
    playerDecision = input()
    if playerDecision == 'Y':
         True
    if playerDecision == 'N':
            sys.exit()
    while True:  
        print("Please enter one of the following below - r(ock), p(aper), s(cissors), q(uit)")
        playerMove = input()
        if playerMove == 'r':
            print("ROCK versus...")
        elif playerMove == 'p':
            print("PAPER versus...")
        elif playerMove == 's':
            print("SCISSORS versus...")
        elif playerMove == 'q':
            print("QUIT")
            sys.exit()

        randomNumber = random.randint(1,3)
        if randomNumber == 1:
            computerMove = 'r'
            print("ROCK")
        elif randomNumber == 2:
            computerMove = 'p'
            print("PAPER")
        elif randomNumber == 3: 
            computerMove = 's'
            print("SCISSORS")

    # display the results
        if playerMove == computerMove: 
            print("You and the computer have tied!")
            ties = ties + 1
            break
        elif playerMove == 'r' and computerMove == 's':
            print("You won!")
            wins = wins + 1 
            break
        elif playerMove == 'p' and computerMove == 'r':
            print("You won!")
            wins = wins + 1
            break
        elif playerMove == 's' and computerMove == 'p':
            print("You won!")
            wins = wins + 1 
            break
        elif playerMove == 'r' and computerMove == 'p':
            print("You lost!")
            losses = losses + 1
            break
        elif playerMove == 'p' and computerMove == 's':
            print("You lost!")
            losses = losses + 1
            break
        elif playerMove == 's' and computerMove == 'r':
            print("You lost!")
            losses = losses + 1
            break
        

        
        


