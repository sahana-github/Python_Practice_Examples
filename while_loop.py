a = 100
while a > 0:
    print(a)
    a //= 5
command = ""
while command.lower() != "quit":
    command = input(":")
    print("You Have Entered", command)
