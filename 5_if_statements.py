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

#omitting the else block, if we used an if-else-block the code would stop running after one passes
requested_toppings = ['mushrooms', 'extra_cheese']
if 'mushrooms' in requested_toppings:
    print("adding mushrooms")
if 'pepperoni' in requested_toppings:
    print("adding pepperoni")
if 'extra_cheese' in requested_toppings:
    print("adding extra cheese.") 

print("\nFinished making your pizza!")

#5-3 
try:
    alien_color_input = input("Alien Color: ")
    if alien_color_input == 'green':
        print("You have just earned 5 points")

except ValueError:
    print("Please enter a valid color:  ")

#5-4 use 
alien_color = "green"

if alien_color == 'yellow':
    print("You have just earned 5 points")
else: 
    print("You have just earned 10 points")

#now use else
alien_color = "blue"

if alien_color == 'yellow':
    print("You have just earned 5 points")
else: 
    print("You have just earned 10 points")

#5-5 
alien_color_input = input("Enter Color: ")
if alien_color_input == "green":
    print("You have earned 5 points")
elif alien_color_input == "yellow":
    print("You have earned 10 points")
elif alien_color_input == "red": 
    print("You have earned 15 points")
else: 
    print("Please enter a valid color") 


#5-6 #int converts any input into an integer. If it can't be processed into an integer it goes straight to ValueError
try:
    person_age = int(input("Enter Your Age: "))
    if person_age <= 2:
        print("You are a baby")
    elif 2<= person_age <4:
        print("This person is a Toddler")
    elif 4<= person_age <13:
        print("This person is a Kid")
    elif 13<= person_age <20:
        print("This person is a Teenager")
    elif 20<= person_age <65:
        print("This person is an Adult") 
    elif person_age >= 65:
        print('You are an Elder')
    else: 
        print("Please enter a valid number")  

except ValueError:
    print("Please enter a valid number") 

#5-7 
favorite_fruit = input("Enter Favorite Fruit:    ")
if 'peaches' == favorite_fruit:
    print(f"You really like {favorite_fruit}")
elif 'mangos' == favorite_fruit:
    print(f"You really like {favorite_fruit}")
elif 'pineapple' == favorite_fruit:
    print(f"You really like {favorite_fruit}")
else:
    print("Please try again")
    favorite_fruit = input("Enter Favorite Fruit:    ")
    '''
'''
#using if statements with lists
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese'] 

for i in requested_toppings:
    print(f"Adding {i}.")

print("\nFinished Making Your Pizza")

#now what if the pizzeria runs out of green peppers? An if statement inside the foor loop can handle this situation appropriately 
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese'] 

for i in requested_toppings:
    if i == 'green peppers':
        print("Sorry, we are out of green peppers right now")
    else: 
        print(f"Adding {i}.")

print("\nFinished Making Your Pizza") 

#checking that a list is not empty (before running a loop, a user may leave a field empty)
requested_currencies = []

if requested_currencies: 
    for i in requested_currencies:
            print(f"Initiating your exchange of {i}")
    print("Finished your exchange")
else: 
     print("Are you sure there isn't anything you want exhchanged today?")

#using multiple lists. we can utilize lists and if statements to make sure our input makes sense before executing on it 
available_currencies = ['USD', 'EUR', 'BP']
requested_currencies = ['USD', 'EUR', 'BP', 'YEN']

for i in requested_currencies:
      if i in available_currencies:
            print("Yes, we intialize your currency exchange")
else:
    print("Sorry, we do not exchange all of the currencies requested. Please try again")