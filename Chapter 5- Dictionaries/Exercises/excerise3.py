## Exercise 3: Glossary 2 :ballot_box_with_check:
""
glossary ={
    'string':'good as  a reaction',
    'comment':'A not in a python that the python interpreter ignores',
    'list':'A list of collection ina particular order',
    'Loop':'Work through a collection of items,one at a time',
    'dictionary':'A collection of key_value pairs',
    'key':'A First item in a key_value pair in a distionary',
    'Value':'An item associated with a key in a distionary',
    'Conditional test':'A comparsion between two values',
    'Float':'A numerical value with a decimal component',
    'Boleenn expersion':'An expression that evaluates to true or false',
    }

for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")