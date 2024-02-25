while True: 
    print("Who are you?")
    name = input()
    if name != 'Joe':
        print("Please provide a valid name in our system.")
        continue #if name is not joe, go back to start of loop
    while True: #created a nested loop
        print("Hello, Joe. What is the password? (It is a Fish)")
        password = input() 
        if password == "swordfish": 
            print("Access Granted")
        else:
            print("Incorrect Password. Please try again.")
        while True: 
            print("Please enter which Database you would like to continue with.")
            print("mySQL", "MongoDB", "PostGRES")
            myDatabase = input()
            if myDatabase == "mySQL":
                    print("The cheapest option. Excellent")
                    exit()
            elif myDatabase == "MongoDB":
                    print("A pricier option but more speed!")
                    exit()
            elif myDatabase == "PostGRES":
                    print("The best option!")
                    exit()
            else: 
                print("Please try again..")
                continue 
