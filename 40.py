num = int(input("Enter the number:\n"))
# factorial = 1
# for i in range(1, num+1):
#     factorial = factorial*i
# print(f"The factorial of number is{factorial}")
sum = 0
while(num > 0):
    sum += num
    num -= 1
print("The sum is", sum)
