students={}
def addStudents(name,marks):
    students[name]=marks
    print(f"{name} added with marks: {marks}")
def updateMarks(name,marks):
    if name in students:
        students[name]=marks
        print(f"{name} added with marks: {marks}")
    else:
        print(F"{name} not found.")
def deleteStudent(name):
    if name in students:
        students.pop(name)
        print(f"{name} student deleted.")
    else:
        print(F"{name} not found.")
def findToper():
    if not students:
        print("No students available.")
        return
    maxMark=-1
    topper=""
    for name,marks in students.items():
        if marks>maxMark:
            maxMark=marks 
            topper=name
    print(f"Topper is {topper} with marks : {maxMark}")

addStudents("Abdullah",82)
updateMarks("Abdullah",86)   #choka
addStudents("Marium",84)
findToper()
deleteStudent("Abdullah")