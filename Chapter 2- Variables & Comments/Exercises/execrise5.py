"""
Chapter 2, Exercise 5: USB Shopper ☑️
A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each.

Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.

You will to use the arithmetic operators to complete this exercise.

"""
print('Enter the price available=')# Asks the user for the price available
price =float(input())

price_of_USB=6 #Price of a single USB stick
print('A single USB stick costs'+ str(price_of_USB)+'dollars.')

USBs_bought=price// price_of_USB #Calculations
balance=price%price_of_USB

print('You have'+str(price)+'dollars and you can buy'+str(USBs_bought)+'sticks')
print('Balance='+str(balance))