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
destination_list = ['virginia', 'new york', 'massachusetts', 'utah', 'illinois']
sorted_list = sorted(destination_list, key = str.lower)
print(sorted_list) #new sorted list without modifying original list
print(destination_list) #original list not affected 

sorted_list.reverse() #reversed list without modifying original list
print(sorted_list)
print(destination_list) #still unaffected 

destination_list.sort() #sorting and modifying list permanently 
print(destination_list)

destination_list.sort(reverse=True) #sorting and modifying list so it's reversed permanently 
print(destination_list)

#3-9
length_list = len(destination_list)
print (length_list)

