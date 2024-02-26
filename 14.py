import random, sys 

wins = 0
losses = 0
ties = 0

while True: 
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    print("Hello Player, above this message you shall see your current leaderboard standing.")
    while True:
        print("Would you like to continue? (Y / N)")
        playerDecision = input()
        if playerDecision == 'Y':
            continue
        if playerDecision == 'N':
            sys.exit()
            
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

        computerMove = random.randint(1,3)
        if computerMove == 1:
            print("ROCK")
        elif computerMove == 2:
            print("PAPER")
        elif computerMove == 3: 
            print("SCISSORS")

        elif playerMove == computerMove: 
            print("You and the computer have tied!")
            ties = ties + 1
        elif playerMove == 'r' and computerMove == 's':
            print("You won!")
            won = won + 1 
        elif playerMove == 'p' and computerMove == 'r':
            print("You won!")
            won = won + 1
        elif playerMove == 's' and computerMove == 'p':
            print("You won!")
            won = won + 1 
        elif playerMove == 'r' and computerMove == 'p':
            print("You lost!")
            losses = losses + 1
        elif playerMove == 'p' and computerMove == 's':
            print("You lost!")
            losses = losses + 1
        elif playerMove == 's' and computerMove == 'r':
            print("You lost!")
            losses = losses + 1

        
        


