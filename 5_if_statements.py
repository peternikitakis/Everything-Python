#programming often involves examining a set of conditions and deciding which action to take based on those conditions. Python's if statement allows you to examine the current state of a program and respond appropriately to that state. 

cars = ['audi', 'bmw', 'subaru', 'toyota']

for i in cars:
    if i == 'bmw':
        print(i.upper())
    else: 
        print(i.lower())

#conditional tests - is at the heart of every if statement and is an expression that can be evaluated as a True or False

answer = 17
if answer != 42:
    print("That is not the correct answer")

age = 18
if age >= 18:
    print("True")

#checking multiple conditions
age_0 = 22 
age_1 = 23
if age_0 >= 21 and age_1 >= 21:
    print("Meets Age Requirement")

#checking to see if a value is in a list
requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_toppings:
    print("True")

#boolean expressions - either true or false. used to keep track of certain conditions 
game_active = True
can_edit = False 

#if statements 
age = 19
if age >= 19:
    print("Great, you can vote!")
    print("Have you registered yet?")
else: 
    print("Sorry, you are too young to vote")
    print("Please register to vote a soon as you turn 18!")


#if-elif-else chain - python runs each conditional test in order until one passes
age = 12
if age < 4: 
    print("your submission cost is $0")
elif age < 18:
    print("Your admission cost is $25")
else:
    print("your admission cost is $40")

#now lets make this more concise

age = 12
if age < 4:
    price = 0 
elif age < 18: 
    price = 25
else: 
    price = 40

print(f"The price of your admission ticket is ${price}")

#now lets use multiple elif blocks
try:
    score = int(input("Enter your score:  "))
except ValueError: 
    print("Please enter a value numeric score")
    result = None 
else:
    if 1 <= score <= 3:
        result = "Beginner"
    elif 4 <= score <= 7:
        result = "Novice"
    elif 8 <= score <= 9: 
        result = "Elite"
    elif score == 10:
        result = "Legendary"
    print(f"You are at a {result} level. Congrats. Continue onwards!")

#omitting the else block
requested_toppings = ['mushrooms', 'extra_cheese']
if 'mushrooms' in requested_toppings:
    print("adding mushrooms")
if 'pepperoni' in requested_toppings:
    print("adding pepperoni")
if 'extra_cheese' in requested_toppings:
    print("adding extra cheese.") 

print("\nFinished making your pizza!")
