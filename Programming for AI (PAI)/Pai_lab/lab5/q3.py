try:
    n=int(input("Enter the number of elements for the lists: "))
    list1=[]
    list2=[]
    print("enter the elements of list1 seperated by enter key")
    for i in range(n):
        list1.append(input())
    print("enter the elments of list2: ")
    for i in range(n):
        list2.append(input())

    myDic={}
    for i in range(n):
        myDic[list1[i]]=list2[i]

    with open(r"dictionary.txt","w") as fileObj:
        for key, value in myDic.items():
            fileObj.write(f"{key}: {value}\n")

    print("DIctionary created and stored successfully.")
    print("DICTIONARY: ",myDic)

except ValueError as ve:
    print(f"Value Error: {ve}")
except FileNotFoundError:
    print("Error: Could not create/open the file.")
except PermissionError:
    print("Error: You don't have permission to write to the file.")
except IsADirectoryError:
    print("Error: Path refers to a directory, not a file.")
except OSError as e:
    print(f"OS Error: {e}")
except Exception as e:
    print(f"Unexpected Error: {type(e).__name__} - {e}")
else:
    print("Program executed successfully.")
finally:
    print("Program execution completed.")