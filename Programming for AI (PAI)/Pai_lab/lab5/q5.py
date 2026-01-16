import json

def processAgeDictionary():
    try:
        personDic={'Ali': 23, 'Saad': 24, 'Salman': 15, 'Shams': 25, 'Sadiq': 46, 'Hammad': 23}

        with open(r"personData.json","w") as fileObj:
            json.dump(personDic,fileObj)
        print("Dictionary saved to json.")

        with open(r"personData.json","r") as fileObj:
            loadedDic=json.load(fileObj)
       
        maxAge=None
        for age in loadedDic.values():
            if maxAge is None or age>maxAge:
                maxAge=age

        personMaxAge=[]
        for name, age in loadedDic.items():
            if age==maxAge:
                personMaxAge.append(name)
        
        print(f"Maximum Age: {maxAge}")
        print(f"Persons with maximum age: {', '.join(personMaxAge)}")

    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: No permission to access the file.")
    except IsADirectoryError:
        print("Error: Path refers to a directory, not a file.")
    except UnicodeDecodeError:
        print("Error: Could not decode file — check file encoding.")
    except json.JSONDecodeError:
        print("Error: JSON decoding failed.")
    except OSError as e:
        print(f"OS Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {type(e).__name__} - {e}")
    else:
        print("Function executed successfully.")
    finally:
        print("Program execution completed.")

processAgeDictionary()
