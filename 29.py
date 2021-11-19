m1 = int(input("Enter marks 1:\n"))
m2 = int(input("Enter marks 2:\n"))
m3 = int(input("Enter marks 3:\n"))
if(m1 < 33 or m2 < 33 or m3 < 33):
    print("Fail")
if(m1+m2+m3)/2 < 40:
    print("Fail because less than 40")
else:
    print("you are pass")
