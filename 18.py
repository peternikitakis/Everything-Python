import random # import module

def getAnswer(answerNumber): # defining the function getAnswer and setting up a parameter to take in an argument
    if answerNumber == 1: 
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidely so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'
    
r = random.randint(1, 9) # the random.randint function gets called with two arguments. this value is then stored inside r variable
fortune = getAnswer(r) # getAnswer function gets called and we pass in the r argument and store that value at fortune passing the r variable in as an argument to the function and assiging this as a new variable

print(fortune) 