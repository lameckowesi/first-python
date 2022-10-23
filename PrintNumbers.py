#While loop for numbers bewteen 1 to 10
from tokenize import Double


Number = 1
while Number <= 10:
    print(Number)
    Number += 1

#For loop for numbers between 1 to 10 
for number in range(1,11):
    print(f"For loop number {number}")

#While loop for even numbers bewteen 1 to 30
EvenNumber = 2
while EvenNumber <=30:
    print(EvenNumber)
    EvenNumber +=2

#For loop for even numbers between 1 to 30
for figure in range (1,31):
    if figure %2 == 0:
        print(f"ForEven {figure}")

#For loop for odd numbers between 1 to 30
for num in range(1,31):
    if num %2 != 0:
        print(f"Odd number {num}")

#While loop for odd numbers between 1 to 30
number = 1
while number <=30:
    print (f"While loop Odd Number {number}")
    number +=2

#Financial Statement Calculator

def calcFinancialStatement ():
    income = 50000
    marketing = 0.25 * income
    opex = 0.5 * income
    customerAcquisition = 0.25 * income
    customersAcquisitionCost = 5
    customersNumber = customerAcquisition / customersAcquisitionCost
    expenses = marketing + opex + customerAcquisition
    balance = income - expenses

    print (f"Income:  {income}")
    print (f"Marketing:  {marketing}")
    print (f"Customer Acquisition:  {customerAcquisition}")
    print (f"Total Expenses:  {expenses}")
    print (f"No of Customers Acquired: {customersNumber}")
    print (f"Balance:  {balance}")
    
calcFinancialStatement()
