from datetime import date

class Vechile: 
    def __init__(self,make,model,rentalPrice,status):
        self.make=make
        self.model=model
        self.__rentalPrice =rentalPrice
        self.avStatus=status

    def checkAvailability(self):
        return self.avStatus
    def returnVechicle(self):
        self.avStatus=True
        print(f"{self.make} {self.model} has been returned and is now available.")
    def rentVechicle(self):
        if self.avStatus:
            print(f"{self.make} {self.model} has been rented.")
        else:
            print(f"{self.make} {self.model} is not available to rent.")

    def display(self):
        print(f"Vechile Details:")
        print(f"make: {self.make}, model: {self.model}, availability status: {self.avStatus}, rentalPrice: {self.__rentalPrice }")

    def calTotalRental(self,days):
        return self.__rentalPrice*days



class Car(Vechile):
    def __init__(self, make, model, rentalPrice, avstatus=True):
        super().__init__(make, model, rentalPrice, avstatus)

    def display(self):
        print("Car Information:")
        super().display()

class SUV(Vechile):
    def __init__(self, make, model, rentalPrice, avStatus=True):
        super().__init__(make, model, rentalPrice, avStatus)

    def display(self):
        print("SUV Information:")
        super().display()

class Truck(Vechile):
    def __init__(self, make, model, rentalPrice, avStatus=True):
        super().__init__(make, model, rentalPrice, avStatus)

    def display(self):
        print("Truck Information:")
        super().display()




class RentalReservation:
    def __init__(self,customer,vechile,startDate,endDate):
        self.customer = customer
        self.vechile = vechile
        self.startDate = startDate
        self.endDate = endDate
    def calCalDays(self):
        return (self.endDate-self.startDate).days

    def display(self):
        print("Rental Reservation Details:")
        print(f"Customer: {self.customer.name}")
        print(f"Vechile: {self.vechile.make} {self.vechile.model}")
        print(f"Start Date: {self.startDate}")
        print(f"End Date: {self.endDate}")
        print(f"Total Days: {self.calCalDays()}")
        print(f"Total Cost: {self.vechile.calTotalRental(self.calCalDays())}")
    

class Customer:
    def __init__(self,name,contactInfo):
        self.name=name
        self.__contactInfo=contactInfo
        self.rentedVechile=[]

    def addRental(self,reservation):
        self.rentedVechile.append(reservation)

    def displayHistory(self):
        print(f"Rental History for {self.name}: ")
        for i in self.rentedVechile:
            i.display()
        
    def getContactInfo(self):
        return self.__contactInfo
    

def showDetails(obj):
    obj.display()


car1 = Car("Toyota", "Corolla", 4000)
suv1 = SUV("Kia", "Sportage", 7000)
truck1 = Truck("Hino", "300", 14000)

customer1 = Customer("Abdullah", "0331232132")
car1.rentVechicle()
rental1=RentalReservation(customer1,car1,date(2025,9,24),date(2025,10,5))
customer1.addRental(rental1)

showDetails(car1)
showDetails(rental1)
customer1.displayHistory()
car1.rentVechicle()