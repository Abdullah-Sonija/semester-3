num=input("Enter a 4 digit no: ")
while not(num.isdigit() and len(num)==4):
  num=int("Enter a 4 digit no: ")
swapped=num[3]+num[2]+num[1]+num[0]
eNum=""
for  ch in swapped:
  digit=int(ch)
  newDigit=(digit+7)%10
  eNum+=str(newDigit)
print("The entrypted number: ",eNum)