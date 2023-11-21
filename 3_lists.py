#lists      a collection of items in a particulat order. 
#brackets   used for indexing and slicing in sequences 
#braces     used for defining sets and dictionaries 

#list (you don't want users seeing these brackets)
stocks = ['AAPL', 'NVDA', 'AMZN', 'MSFT', 'AMD,']
print(stocks)

#accessing certain elements in a list
stocks = ['AAPL', 'NVDA', 'AMZN', 'MSFT', 'AMD']
print(stocks[1])
print(stocks[1].title())
print(stocks[4].lower())
print(stocks[-1].lower())


#using individual values from the list
message = (f"My favorite stocks picks are {stocks[3].upper()}")
print(message)

#3-1 Books
Books = ['Security +', 'Securing DevOps', 'The Practice of System and Network Administration', 'rhcsa 9']
print(Books[0])
print(Books[-1])

#3-2 bringing it all together 
redhat_message = (f"\tI am currently working through {Books[-1].upper()}")
devsecops_message = (f"\tMy next book will be {Books[1]}") 
sec_plus = (f"\tI have finished {Books[0]} and recieved my certification. It was easy.")
print(redhat_message)
print(devsecops_message)
print(sec_plus)

#modifying elements in a list
car_manufacturers = ['toyota', 'honda', 'subaru']
car_manufacturers[1] = 'nissan'
print(car_manufacturers)

car_manufacturers.append("honda")
print(car_manufacturers)
manufacturers_list = (f"List: {car_manufacturers[0].title()}, {car_manufacturers[2].title()}")
print(manufacturers_list)

#modify list again
car_manufacturers[2] = 'mercedes'
car_manufacturers.remove('nissan')
print(car_manufacturers)

#insert method
car_manufacturers.insert(0, "mclaren")
print(car_manufacturers)

#pop() method removes the last item in a list and lets you work with that item after removing it
popped_manufacturer = car_manufacturers.pop()
print(popped_manufacturer)

#now use pop() and by including the index of the item you want removed. Also use a method include a string 
exotic_manufacturer = (f"The {car_manufacturers.pop(0).title()}")
print(exotic_manufacturer)


