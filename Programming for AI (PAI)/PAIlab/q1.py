var=int(input("Enter a number: "))
varF=float(var)
varS=str(var)
varC=complex(var)
print(f"Integer value: {var} (Type: {type(var)})")
print(f"Float value: {varF} - Type: {type(varF)}")
print(f"String value: {varS} - Type: {type(varS)}")
print(f"Complex value: {varC} - Type: {type}(varC)")
half=var/2
if(half*2==var):
  print("Even Number, divisble by 2.")
else:
  print("Odd Number, not divisible by 2")
