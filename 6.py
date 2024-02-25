name = "" #a variable that holds a string data type but with no characters
while not name: #a loop that continues as long as the condition is not true
        print("Enter your name: ")
        name = input()
print("How many guests will you have?")
numOfGuests = int(input())
if numOfGuests:
        print('Be sure to have enough room for all your guests.')
print('Done')