#Exercise 5: Cities
""
def describe_city(city, country='Switzerland '):
    "Describe a city."
    msg=(f"{city.title()} is in {country.title()}.")
    print(msg)
    
describe_city('Winterthur')
describe_city('Interlaken',)
describe_city('Zurich')