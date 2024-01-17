## Exercise 4: Rivers :ballot_box_with_check:
""
rivers={
        'Mekong River':'Southeast Asia',
        'Volga River':' Europe',
        'Rhine River':'Netherlands.',
        'Ganges River':'Bangladesh',
        'yangtze':'china',
        }

for river, country in rivers.items():
    print(f"the{river.title()}flos through{country.title()}.")
    
    print("\nthe following countries are include in this data set:")
    for country in rivers.values():
        print(F"-{country.title()}")
        
    print("\nthe following rivers are include in this data set:")
    for river in rivers.keys():
            print(F"-{river.title()}")