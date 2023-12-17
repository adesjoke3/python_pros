password = "adekunlefamily!!"


while True:
    user_input = input("Enter the password")
    if user_input == password:
        print("Password accepted. Access granted!")
        break
    else:
        print("Incorrect password.Try again")