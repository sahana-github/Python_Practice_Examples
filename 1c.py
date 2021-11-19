# def Max(list):
#     if len(list) == 1:
#         return list[0]
#     else:
#         m = Max(list[1:])
#         return m if m > list[0] else list[0]


# def main():
#     try:
#         list = eval(input("Enter a list of numbers: "))
#         print("The largest number is: ", Max(list))
#     except SyntaxError:
#         print("Please enter comma separated numbers")
#     except:
#         print("Enter only numbers")


# main()
# Python program to find largest
# number in a list

# creating empty list
list1 = []

# asking number of elements to put in list
num = int(input("Enter number of elements in list: "))

# iterating till num to append elements in list
for i in range(1, num + 1):
	ele = int(input("Enter elements: "))
	list1.append(ele)
	
# print maximum element
print("Largest element is:", max(list1))
