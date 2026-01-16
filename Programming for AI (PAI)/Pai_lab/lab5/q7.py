def fixFile():
    try:
        with open(r"replacement_needed.txt","r") as fileObj:
            content=fileObj.read()
        Ichar=input("Enter the character to be repalced: ")[0]
        Ochar=input("Enter the new character: ")[0]
            
        replaced=False
        correctedContent=""

        for char in content:
            if char==Ichar and not replaced:
                correctedContent+=Ochar
                replaced=True
            else:
                correctedContent+=char

        with open(r"replacement_needed.txt","w") as fileObj:
            fileObj.write(correctedContent)

        print("File corrected successfully!")
        print("Corrected content:", correctedContent)

    except FileNotFoundError:
        print("Error: The file was not found.")
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
        print("Function executed successfully.")
    finally:
        print("Program execution completed.")


fixFile()