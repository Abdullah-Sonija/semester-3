class Vechile:
    def __init__(self,capacity): 
        self.seatingCapacity=capacity
    def fare(self):
        return self.seatingCapacity*100
    def display(self):
        print(f"Total fare : {self.fare()}")

class Bus(Vechile):
    def fare(self):
        baseFare=super().fare()
        totalFare=baseFare+(0.1*baseFare)
        return totalFare
    def display(self):
        print(f"Total fare : {self.fare()}")

bus=Bus(50)
bus.display()