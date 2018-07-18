# input() is used to input from console
# input() returns value as string hence need to convert it to int() for interger comparison

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

if num1 > num2:
    print(num1, " is greater than ", num2)
else:
    print(num2, " is greater than ", num1)
