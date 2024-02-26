import random, sys
computerMove = random.choice(['ROCK', 'PAPER', 'SCISSORS'])

wins = 0
losses = 0
ties = 0 

while True:
    print("Enter your move: (r)ock, (p)aper, (s)cissors, or (q)uit.")
    playerMove = input()

    print("Your Move: " + playerMove)
    if playerMove == "r" and computerMove == "ROCK": # if player picks rock and opponent picks rock
        print("Opponents Move : " + computerMove)
        print("It is a tie!")
        ties = ties + 1
        print(str(wins) + " Wins", str(losses) + " Losses", str(ties) + " Ties")
    elif playerMove == "r" and computerMove == "PAPER": # if player picks rock and opponent picks paper
        print("Opponents Move : " + computerMove)
        print("You lost!")
        losses = losses + 1
        print(str(wins) + " Wins", str(losses) + " Losses", str(ties) + " Ties")
    elif playerMove == "r" and computerMove == "SCISSORS": # if player picks rock and opponent picks scissors
        print("Opponents Move : " + computerMove)
        print("You won!")
        wins = wins + 1
        print(str(wins) + " Wins", str(losses) + " Losses", str(ties) + " Ties")
    elif playerMove == "p" and computerMove == "PAPER": # if player picks paper and opponent picks paper
        print("Opponents Move : " + computerMove)
        print("It is a tie!")
        ties = ties + 1
        print(str(wins) + " Wins", str(losses) + " Losses", str(ties) + " Ties")
    elif playerMove == "p" and computerMove == "SCISSORS": # if player picks paper and opponent picks scissors
        print("Opponents Move : " + computerMove)
        print("You lost!")
        losses = losses + 1
        print(str(wins) + " Wins", str(losses) + " Losses", str(ties) + " Ties")
    elif playerMove == "p" and computerMove == "ROCK": # if player picks paper and opponent picks rock
        print("Opponents Move : " + computerMove)
        print("You won!")
        wins = wins + 1
        print(str(wins) + " Wins", str(losses) + " Losses", str(ties) + " Ties")
    elif playerMove == "s" and computerMove == "SCISSORS": # if player picks scissors and opponent picks scissors
        print("Opponents Move : " + computerMove)
        print("It is a tie!")
        ties = ties + 1
        print(str(wins) + " Wins", str(losses) + " Losses", str(ties) + " Ties")
    elif playerMove == "s" and computerMove == "PAPER": # if player picks scissors and opponent picks paper
        print("Opponents Move : " + computerMove)
        print("You lost!")
        losses = losses + 1
        print(str(wins) + " Wins", str(losses) + " Losses", str(ties) + " Ties")
    elif playerMove == "s" and computerMove == "ROCK": # if player picks scissors and opponent picks rock
        print("Opponents Move : " + computerMove)
        print("You won!")
        wins = wins + 1
        print(str(wins) + " Wins", str(losses) + " Losses", str(ties) + " Ties")
    elif playerMove == "q":
        print("This game will now quit!")
        break
    else:
        print("Please enter a valid move.")
        break


