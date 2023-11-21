#Variables: name = ada lovelace
#Methods:   .title() -> is an action that python can perform on a piece of data, . after tells python to act on variable
#Strings:   "Hello, my friend" -> a series of characters that is held within quotes 
#Syntax:    A syntax error occurs when Python doesn't recognize a section of your program 


#variables, methods, strings, and f strings
first_name = "peter"
last_name = "nikitakis"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}." + " Your seat awaits you."
intro = f"We are waiting for a few more. {message}" + " The show shall start soon."
print(f"\t{intro} I heard it will be quite the experience. Ludovico is starring.")

#add a tab to your text 
print('\t' + "It's a masterpiece.")

#to add a newline in a string, use the character combination \n:
print("\tThank you.\n \tIt's been a pleasure.\n")

#chaning a variable's value
favorite_lang = "Python "
favorite_lang.strip()
print(favorite_lang)

#removing prefixes
aws_url = 'https://aws.console.com'
new_url = aws_url.removeprefix('https://')
print(new_url)

#try it yourself

#2-3 personal message
person_name = "Eric"
print(f"Hello {person_name}, would you like to learn some Python today?")

#2-4 name cases
student = "peter"
print(student.lower())
print(student.upper())
print(student.title())

#2-5 famous quote 
print("Alexander The Great once said, I had rather excel others in the knowledge of what is excellent, than in the extent of my power and dominion.")

#2-6 famous quote but with using a variable
famous_person = "Alexander The Great"
famous_quote = "I had rather excel others in the knowledge of what is excellent, than in the extent of my power and dominion."
print(f"{famous_person} once said, {famous_quote}")

#2-7 stripping names 
temp_name = " Peter "
print(temp_name.lstrip())
print(temp_name.rstrip())
print(temp_name.strip())
print(f"\n{temp_name}")
print(f"\t{temp_name}")

#2-8 File Extension
filename = "python_notes.txt"
print(filename.removesuffix(".txt"))
    
#numbers, integers, floats, underscores
world_age = 12_000_000_000
print(world_age)\

#multiple assignment
x, y, z = 0, 0, 0

#constants
MAX_CONNECTIONS = 5000
print(MAX_CONNECTIONS)

#2-9
print(4+4)
print(12-4)
print(4*2)
print(16/2)
master_number = 22
print(f"My master number {master_number}")


