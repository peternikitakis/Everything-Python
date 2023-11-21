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
Books = ['Security +', 'Securing DevOps', 'The Practice of System and Network Administration', 'RHCSA 9']
print(Books[0])
print(Books[-1])

redhat_message = (f"\tI am currently working through {Books[-1]}")
devsecops_message = (f"\tMy next book will be {Books[1]}") 
sec_plus = (f"\tI have finished {Books[0]} and recieved my certification. It was easy.")
print(redhat_message)
print(devsecops_message)
print(sec_plus)

