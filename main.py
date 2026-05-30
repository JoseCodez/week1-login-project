print("=== LOGIN SYSTEM ===")
name = input("Enter your name: ")
if name == "Jose":
    print("Welcome back admin")
else: 
    print("Welcome user")

attempts = 3
while attempts > 0:
    password = input("Enter password: ")
    if password == "2805":
        print("Access granted")
        print("Access granted")
        print("=== ADMIN MENU ===")
        print("1. View system status")
        print("2. Logout")
        choice = input("Choose an option: ")
        if choice == "1":
            print("System online")
        elif choice == "2":
            print("Logged out")
        else:
            print("Invalid option")
        break
    else:
        attempts = attempts - 1
        print("Wrong password. Attempts left:", attempts)
        if attempts == 1:
            print("Hint: My birthday")
if attempts == 0:
    print("Account locked")

       
       
              
       








