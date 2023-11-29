#slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])

#omit the first index or last index - automatically starts at the beginning of the list or end
print(players[:4])
print(players[2:])

#looping through a slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players of the team")
for player in players[0:3]:
    print(player.title())

#copying a list
my_foods  = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print(f"\nMy favorite foods are {my_foods}")
print(f"\nMy friend's favorite foods are: {friend_foods}")

#two prove we now have two separate lists
my_foods.append("cannoli")
friend_foods.append("ice cream")
print(my_foods)
print(friend_foods)

#if we were simply to make a new variable (friends_food = my_foods without indexing the list [:] it wouldn't have created a new list

#4-10
master_numbers = ['11', '22', '33']
print (f"The first two numbers are {master_numbers[0:2]}")

#4-11 
my_numbers = ['1', '9', '22']
friends_numbers = my_numbers[:]
print(f"My friend's numbers are: {friends_numbers}")

my_numbers.append("44")
friends_numbers.append("55")

print("\nmy numbers are:")
for i in my_numbers:
    print(i)

print("\nmy friend's numbers are:")
for i in friends_numbers:
    print(i)

#lists work well for storing collections of items that can change throughout the life of a program. The ability to modify lists in important when working with a list of users on a website or a list of characters in a game. However, sometimes you'll want to 

#defining a tuple = looks just like a list, except you use parentheses instead of square brackets. Once you define a tuple, you can access individual elements by using each item's index, just as you would for a list. 

#for example, if we have a rectange that should always be a certain size, we can ensure its size does not change by putting the dimensions into a tuple 

dimensions = (200, 50)
print("\n")
print(dimensions[0])
print(dimensions[1])

#looping through all values in a tuple
for i in dimensions:
    print(i)


