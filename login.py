print("Log in Details:")
username = "sahana"
password = 123
username = str(input("username: "))
password = int(input("password: "))

# if(username and password):
#   print("Password entered is correct")
# else:
#   print("Password entered is Incorrect")
message = "Correct" if username and password else "Incorrect"
print(message)
