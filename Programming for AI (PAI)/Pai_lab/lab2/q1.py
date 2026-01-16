def isValidPassword(password):
    if len(password)>=8:
        hasLetter=any(c.isalpha() for c in password)
        hasDigit=any(c.isdigit() for c in password)
        hasSpecial=any(c in "!@#$%*" for c in password)
        return hasLetter and hasDigit and hasSpecial
    

password=input("Enter the Password: ")
if isValidPassword(password):
    print("Valid password")
else:
    print("Invalid password.")