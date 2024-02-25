print("Hello, welcome to the game. Please first start by entering in your previous score to detemrine your rank.")


while True: 
    print("What is your previous score?")
    myScore = int(input())

    if myScore <= 5:
        print("You are a Lieutenant.")
        break
    elif myScore <=10:
        print("You are a General.")
        break
    elif myScore <=15:
        print("You are a Major.")
        break
    elif myScore <=20: 
        print("you are a Colonel") 
        break
    else:
        print("Please provide a valid score that is within the range of 1-20")

