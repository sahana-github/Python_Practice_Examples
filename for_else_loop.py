sucessful = True  # if it is true then prints message sent sucessful

for number in range(3):
    print("Attempt")
    if sucessful:
        print("Message sent sucessfull")
        break
else:
    print("Tried 3 attempts but failed")
