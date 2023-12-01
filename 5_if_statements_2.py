#end of chapter project 
user_login = input("Username:  ")
user_names = ['guest', 'admin', 'financial', 'marketing', 'management', 'developer' ]

for i in user_names:
    if i == user_login:
        print(f"Hello, {i}. would you like to see a status report?")
        break
else:  
    print(f"Hello {user_login}, thank you for trying to sign in. Please sign in as an authorized user.")

#clearing list and turning list into a string so brackets disappear 
user_names[0:6] = []

#importing and setting the duration of time 
import time

time_duration = 5
print("Loading..")
time.sleep(time_duration)

if not user_names:
    print("We need to authorize you as a user. Let's first search our database.")

#lowering time duration
time_duration = 2 
time.sleep(time_duration) 

print("Searching..")
time_duration = 1
time.sleep(time_duration)

print("Users found! Please search for your name again")
current_users = ['ben', 'max', 'john', 'greg']


while True:
    user_login = input("Username:  ")

    username_taken = False #resets to false after loop

    for i in current_users:
                if i == user_login:
                    print(f"You will need to enter a new username as this had already been taken. Please try again.")
                    username_taken = True
                if not username_taken:
                    claim_username = input(f"Great. {user_login} is available. Would you like to claim the username? (yes/no):  ")
                    if claim_username.lower() == 'yes':
                        print(f"Great the {user_login} has been successfully added")
                        current_users.append(user_login)
                    else:
                        print("Thank you for your answer. This program will now shutdown.")
                        break

        