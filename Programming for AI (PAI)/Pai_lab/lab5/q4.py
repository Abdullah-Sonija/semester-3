try:
    name=input("Enter the name: ")
    cnic=input("Enter the CNIC: ")
    age=input("Enter the age: ")
    salary=input("Enter the salary: ")

    with open(r"Employees.txt","w") as fileObj:
        fileObj.write(f"Name: {name}\n")
        fileObj.write(f"CNIC: {cnic}\n")
        fileObj.write(f"Age: {age}\n")
        fileObj.write(f"Salary: {salary}\n")

    print("Biodata saved successfully!")

    contact=input("Enter the contact No: ")
    with open(r"Employees.txt","a") as fileObj:
        fileObj.write(f"Contact: {contact}\n")
    
    print("Contact number appended successfully!")

    with open(r"Employees.txt", "r") as fileObj:
        print("\n--- Employee File Contents ---")
        content = fileObj.read()
    print(content)


except FileNotFoundError:
    print("Error: Could not find or create the file.")
except PermissionError:
    print("Error: You don't have permission to access this file.")
except IsADirectoryError:
    print("Error: Path refers to a directory, not a file.")
except UnicodeDecodeError:
    print("Error: Could not decode file — check file encoding.")
except OSError as e:
    print(f"OS Error: {e}")
except Exception as e:
    print(f"Unexpected Error: {type(e).__name__} - {e}")
else:
    print("Program executed successfully.")
finally:
    print("Program execution completed.")
