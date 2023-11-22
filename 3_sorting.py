# sorting 
# argument  an argument is can be a value that's passed through a method or function when called 

#sorting a list permanently with the sort() method. sorts alphabetically 
cars = ['bmw', 'audi', 'mercedes']
cars.sort()
print(cars)

#passing an argument through the method 
cars.sort(reverse=True)
print(cars)

#sorting a list temporarily with the sorted() function 
cars = ['bmw', 'audi', 'mercedes']
print("Here is the original list: ")
print(cars)

print("\nHere is the sorted list: ")
print(sorted(cars))

#printing in reverse permanently 
cars = ['bmw', 'audi', 'mercedes']
cars.reverse()
print(cars)

#finding list length
li = len(cars)
print(li)

#3-8 
