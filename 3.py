print("Hello, user 1 - What is your name?")

myName = input()
print("Great. Thank you for that information. Next...")

print("What is your age?")
myAge = (int(input()))


try: 
    if myName == "Alice" and myAge <=12:
        print("Hello, Alice. Thank you for participating.")
    elif myAge >=12:
        print("You are not Alice! Imposter!")

except ValueError:
    print("Invalid input. Please enter a valid age.")