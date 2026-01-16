
try:
    with open(r"text.txt","r") as fileObj:
        content=fileObj.read()
        charCount=len(content)
        wordCount=len(content.split())
        print(f"Total Characters: {charCount}")
        print(f"Total Words: {wordCount}")

except FileNotFoundError:
    print("Error: The file was not found.")
except PermissionError:
    print("Error: You don't have permission to access this file.")
except IsADirectoryError:
        print("Error: The given path refers to a directory, not a file.")
except UnicodeDecodeError:
    print("Error: Could not decode file — check file encoding.")
except OSError as e:
    print(f"OS Error: {e}")
except Exception as e:
     print(f"Unexpected Error: {type(e).__name__} - {e}")

else:
    print("File processed successfully.")
finally:
    print("Program execution completed.")