# working with lists
# for loop
#indentation - the only lines 
#range() - makes it easy to generate a series of numbers 
'''
#defining a for loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

#adding what we learned prior
for magician in magicians: 
    print(f"{magician.title()}, that was a great trick")

#adding indenentation
    print(f"I'm looking forward to your next trick, {magician.title()}\n")'''

#4-1 
pizzas = ['pepperoni', 'pinapple & ham', 'sausage']
for pizza in pizzas:
    print(f"I like {pizza} pizza")

print("\nYes, I really like pizza.\n")

#4-2 
animals = ['eagle', 'falcon', 'hawk']
for animal in animals:
    print(f"A {animal} would make a great pet")

print("\nAny of these animals would make a great pet.")

#using the range function 
for value in range(1,5):
    print(value)

for value in range(1,6):
    print(value)

#using range() to make a list of mnumbers
numbers = list(range(1,6))
print(numbers)

#creating a range of numbers and adding increments 
even_numbers = list(range(2, 11, 2))
print(even_numbers)

#here is an empty list called squares. we then tell python to loop through each value from 1 to 10 using the range() function. Inside the loop, the current value is raised to the second power and assigned to the variable square. For each new value its then appended to the list squares
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

#now to write this code more concisely.. 
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
    print(squares)

#list comprehensions 
squares = [value**2 for value in range (1, 11)]
print(squares)

#4-3 counting to twenty
for value in range(1, 21):
    print(value)


#4-4 one million 
for value in range(1, 101):
    print(value) 

#4-5 making a list from one to one million, and then use min() max() and sum() function 
my_list = list(range(1, 101))
print(min(my_list))
print(max(my_list))
print(sum(my_list))

#4-6 odd numbers
my_odd_list = list(range(1, 21, 2))
for i in my_odd_list:
    print(i)

#4-7 threes
multiple_list = list(range(3, 30, 3))
for i in multiple_list:
    print(i)

#4-8 
cube_list = list(range(1, 11))
for i in cube_list:
    print(i**3)

#4-8 same result but writing code more concisely. Also included a string 
for i in range(1, 11):
    print("{} cubed is {}".format(i,i**3))

#4-9 use a list comprehension to generate a list of the first 10 cubes
cubed_list = [i **3 for i in range(1, 11)]
print(cubed_list)
