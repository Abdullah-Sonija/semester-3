class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary

    def getSalary(self):
        return self.__salary

    def calBonus(self):
        pass


class Manager(Employee):
    def calBonus(self):
        return self.getSalary()*.2
    
    def hire(self):
        print(f"{self.name} (Manager) is hiring someone.")


class Developer(Employee):
    def calBonus(self):
        return self.getSalary()*0.1
    
    def writeCode(self):
        print(f"{self.name} (Developer) is writing code.")


class SeniorManager(Manager):
    def calBonus(self):
        return self.getSalary()*0.3


m = Manager("Abdullah", 100000)
d = Developer("Ahmed", 80000)
s = SeniorManager("Usman", 150000)

print("Manager Bonus:", m.calBonus())
m.hire()
print("Developer Bonus:", d.calBonus())
d.writeCode()
print("Senior Manager Bonus:", s.calBonus())
