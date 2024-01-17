# Exercise 4: Deli :ballot_box_with_check:
""
sandwich_orders=['tikka ','spicy chilli','chicken ranch','veggei with mayo']
finished_sandwiches=[]

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm working on your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)
    
print("\n")
for sandwich in finished_sandwiches:
    print(f" your order is ready. {sandwich} sandwich.")