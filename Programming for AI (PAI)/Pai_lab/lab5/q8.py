try:
    num1=int(input("Enter the 1st number: "))
    num2=int (input("Enter the 2nd number: "))

    result=num1/num2
    print(f"Result: {result}")

except ZeroDivisionError:
    print("ERROR: Trying to divide by zero.")
except ValueError:
    print("ERROR: Invalid Input please enter the integer value.")
except Exception as e:
    print(f"Unkwnon Error occured: {type(e.__name__)} - {e}")

else:
    print("Division performed successfully.")
finally:
    print("Program execution completed.")