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

#3-4 create guest list and an invitation for each
guest_list = ['John', 'Alex', 'Joseph']
message_one = (f"Dear {guest_list[0]}, would you like to attend the show?")
message_two = (f"Dear {guest_list[1]}, would you like to attend the show?")
message_three = (f"Dear {guest_list[2]}, would you like to attend the show?")

print(f"Unfortunately, it appears that {guest_list[1]} can't make the show, but we may have someone else. ")

#3-5 changing guest list - removed alex and added greg in index spot 1 + resent out invitations
guest_list[1] = ("Greg")
message_two = (f"Dear {guest_list[1]}, would you like to attend the show?")

print("Oh look guys! I found three more tickets.")

#3-6 invite more people to the show
guest_list.insert(0, "Tom")
guest_list.insert(2, "Ben")
guest_list.append("Patrick")

message_four = (f"Dear {guest_list[0]} would you like to attend the show?")
message_five = (f"Dear {guest_list[2]} would you like to attend the show?")
message_six = (f"Dear {guest_list[5]} would you like to attend the show?")


print(message_one)
print(message_two)
print(message_three)
print(message_four)
print(message_five)
print(message_six)

print("Oh no, it says the max number of participants I can bring are two")

# popping out each person I am rescinding the invite to and sending them a message apologizing 
pop_invite = guest_list.pop(0)
invite_withdraw_01 = (f"Dear {pop_invite}, I am sorry you can no longer attend. I can only bring two people.")

pop_invite_02 = guest_list.pop(1)
invite_withdraw_02 = (f"Dear, {pop_invite_02}, I am sorry you can no longer attend. I can only bring two people.")

pop_invite_03 = guest_list.pop(3)
invite_withdraw_03 = (f"Dear, {pop_invite_03}, I am sorry you can no longer attend. I can only bring two people.")

pop_invite_04 = guest_list.pop(0)
invite_withdraw_03 = (f"Dear, {pop_invite_04}, I am sorry you can no longer attend. I can only bring two people.")

'''pop_invite_04 = guest_list.pop(4)
invite_withdraw_03 = (f"Dear, {pop_invite_04}, I am sorry you can no longer attend. I can only bring two people.")'''

print(invite_withdraw_01)
print(invite_withdraw_02)
print(invite_withdraw_03)

print(f"Dear {guest_list[0]}, while I had to rescind my invite to others, please do still accept my invitation.")
print(f"Dear {guest_list[1]}, while I had to rescind my invite to others, please do still accept my invitation.")

#remove everyone off list and show list is empty 
del guest_list[0]
del guest_list[0]
print(guest_list)