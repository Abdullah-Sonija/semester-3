def saveQuestion():
    try:
        sentence = input("Enter a sentence: ")

        if sentence.strip().endswith("?"):
            with open(r"questions.txt", "a") as fileObj:  
                fileObj.write(sentence + "\n")
            print("Question saved successfully!")
        else:
            print("Not a question. Nothing saved.")

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
        print("Function executed successfully.")
    finally:
        print("Program execution completed.")


saveQuestion()
