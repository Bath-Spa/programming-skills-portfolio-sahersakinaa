## Exercise 1: Pizza Toppings :ballot_box_with_check:
""
prompt="\nwhat topping would you like on your pizza?"
prompt+="\nenter'00' when you are finished:"

while True:
    topping=input(prompt)
    if topping!='00':
        print(" I'll add{topping} to your pizza.")
    else:
        break