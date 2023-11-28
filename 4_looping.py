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

#a list of the first 10 square numbers
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

