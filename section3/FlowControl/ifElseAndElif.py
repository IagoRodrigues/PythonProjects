"""
For this problem you are going to make a program that simulates the output of a vending machine that only takes in
coins of American currency.
1.Your program should take an integer as an input from the user (either a 1, 2, or 3) that corresponds with an option
for a drink from the vending machine outlined below and assign the corresponding price to a variable as a float.
Use your knowledge of if, elif, and else statements to complete this part of the problem. Your code should
have an else statement that prints a message and ends the program using sys.exit() if the user does not enter a valid
input number.
Vending Machine:
1.water = $1.00
2.cola = $1.50
3.gatorade = $2.00
2.After placing an order, the user should be prompted to enter inputs 4 times:
1.The first time, the user should be prompted to enter the number of quarters they put in the machine. Assign this
number to a variable as an integer.
2.The second time, the user should be prompted to enter the number of dimes they put in the machine. Assign this
number to a variable as an integer.
3.The third time, the user should be prompted to enter the number of nickles they put in the machine. Assign this
number to a variable as an integer.
4.The fourth time, the user should be prompted to enter the number of pennies they put in the machine. Assign this
number to a variable as an integer.
3.Create a variable to hold the total value of all the coins the user has put into the machine.
4.Use flow control statements to print the user's change or output a message asking the user to try again depending
on whether the total value of the coins the user has put into the machine is enough to pay for the item they ordered.
New knowledge for this problem:
1.%f format specifier
2.import sys and sys.exit()
3.int()

quarter is worth 25 cents (25% of a dollar), a dime is worth 10 cents (10% of a dollar), a nickel is 5 cents
(5% of a dollar and a penny is 1 cent (1% of a dollar)
"""
import sys

opt = int(input("1.water = $1.00\n2.cola = $1.50\n3.gatorade = $2.00\n"))

quarter = int(input("Valor em quarter: \n"))
dime = int(input("Valor em dime: \n"))
nickel= int(input("Valor em nickel: \n"))
penny= int(input("Valor em penny: \n"))

total = (quarter * 0.25) + (dime * 0.1) + (nickel * 0.5) + (penny * 0.01)

if opt == 1:
    troco = total - 1
elif opt == 2:
    troco = total - 1.50
elif opt == 3:
    troco = total - 2
else:
    print("Erro-> Tente novamente!!")
    print("Total devolvido: %.2f"% total)
    sys.exit()

if troco < 0:
    print("Erro-> Valor inserido baixo demais!!")
    print("Total devolvido: %.2f"% total)
else:
    print("Obrigado, tenha um bom dia!!")
    print("Total devolvido: %.2f"% troco)