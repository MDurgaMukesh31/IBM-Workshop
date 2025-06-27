user_data = ("admin", "1234")
input_username = input("Enter username: ")
input_password = input("Enter password: ")
if (input_username, input_password) == user_data:
    print("Login successful!")
else:
    print("Invalid username or password.")
