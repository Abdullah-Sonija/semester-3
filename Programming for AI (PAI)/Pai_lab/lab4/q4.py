class Student:
    def __init__(self,name,id):
        self.name=name
        self.ID=id
    def display(self):
        print(f"Student Name {self.name}, ID : {self.ID}")
    
class Marks(Student):
    def __init__(self, name, id, marks_list):
        super().__init__(name, id)
        self.marksList=marks_list

    def display(self):
        super().display()
        print(f"Marks Obtained: ")
        for i,mark in enumerate(self.marksList,start=1):
            print(f" Course[i]: {mark}")

class Result(Marks):
    def __init__(self, name, id, marks_list):
        super().__init__(name, id, marks_list)
    def display(self):
        super().display()
        print(f"Result: Total Marks: {sum(self.marksList)} Average: {sum(self.marksList)/len(self.marksList)}")
    
marks = [85, 90, 86] 
student1 = Result("Abdullah", "24K-0013", marks)
student1.display()