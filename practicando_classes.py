class Vehicles: 
    """Modeling a vehicle maximun speed and milage"""
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = 'White'
    
    def description_vehicle(self):
        print(f"color: {self.color}, vehicle: {self.name} maximun speed: {self.max_speed} mileage: {self.mileage}")

    def capacity(self, capacity):
        print(f"The seating capacity of a {self.name} is {capacity} passengers")

    def fare(self):
        capacity = int(self.capacity)
        print(capacity * 100)


class Bus(Vehicles):
    """Bus class inheritance from vehicles"""
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)
        self.seating_capacity = 50

    def capacity(self, capacity = 50):
        print(f"The seating capacity of a {self.name} is {capacity} passengers")

    def fare(self):
        print(self.capacity * 100)


small_car = Vehicles('mazda', 120, 3000)
small_car.description_vehicle()
small_car.capacity(4)
small_car.fare()

scolar_bus = Bus('bus',200, 2000)
scolar_bus.description_vehicle()
scolar_bus.capacity()
scolar_bus.fare()



    

