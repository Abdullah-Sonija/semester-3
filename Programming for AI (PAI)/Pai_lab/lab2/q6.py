countries = {
    "China": 1440,
    "India": 1390,
    "USA": 331,
    "Indonesia": 276,
    "Pakistan": 225
}
top3=[]
for i in range(3):
    maxCountry=max(countries,key=countries.get)
    top3.append((maxCountry,countries[maxCountry]))
    countries.pop(maxCountry)
print(f"Top 3 most populated Countires are: {top3}")
