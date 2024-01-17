# Exercise 5: No Pastrami :ballot_box_with_check:
""
sandwich_orders={
    'tikka','veggei with mayo','spicy chilli','chicken ranch','egg with chesse','mutton',
    }
finished_sandwiches={}

print("I'm sorry, we're all out of mutton today.")
while 'mutton' in sandwich_orders:
    sandwich_orders.remove('mutton')
    
    print("\n")
    while sandwich_orders:
        current_sandwich = sandwich_orders.pop()
        print(f"I'm working on your {current_sandwich} sandwich.")
        finished_sandwiches.append (current_sandwich)
        
        print("\n")
        for sandwich in finished_sandwiches:
            print(f" your order is ready {sandwich} sandwich.")