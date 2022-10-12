import colorama
from colorama import init,Fore,Back
init(convert=True)
print("Hello buddy, lets do some math! Integers only,okay?")
num1=int(input("Enter First Number: "))
num2=int(input("Enter Second Number: "))
sum=num1+num2
print(num1,"+",num2,"=",sum)
print("Okay, now let's try it with decimal numbers")
num3=float(input("Enter First Decimal Numbver:  "))
num4=float(input("Enter Second Decimal Number:  "))
sum2=num3+num4
print("The sum of",num3,"and",num4,"is",sum2)