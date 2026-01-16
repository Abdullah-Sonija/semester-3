name = input("Enter your name: ")
year = input("Enter your birth year: ")
while len(name) < 3 or not (year.isdigit() and len(year) == 4):
    print("Invalid input!")
    name = input("Enter your name: ")
    year = input("Enter your birth year: ")
first_three = name[:3]
first_three = first_three[0].upper() + first_three[1].lower() + first_three[2]
last_two = year[-2:]
symbols = "@#%&*"
ascii_val = ord(name[0])
index = ascii_val % len(symbols)
special_symbol = symbols[index]
password = first_three + last_two + special_symbol
print(f"Generated password: {password}")
