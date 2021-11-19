a = str(input("Enter a string: "))


def func1(para):

    n = str(input("enter the character to find the index: "))
    # print(a.find(n))
    print(a.index(n))
    print("Length of the string is:")
    leng = len(a)
    print(leng)


func1(a)
