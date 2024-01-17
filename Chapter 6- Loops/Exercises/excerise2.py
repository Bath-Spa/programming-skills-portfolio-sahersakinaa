## Exercise 2: Movie Tickets: :ballot_box_with_check:
""
prompt="Movie Tickets"
prompt+="\n enter'END'when you are finished."

while True:
    age=input(prompt)
    if age =='END':
        break
        age=int(age)
        
        if age<4:
            print("you get is free ticket.")
        elif age<14:
            print("Your ticket is $10.")
        else:
            print("Your ticket is $15.")