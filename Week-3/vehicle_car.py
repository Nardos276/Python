class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def info(self):
        print(self.brand, self.year)
class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model

    def info(self):
        print(self.brand, self.model, self.year)
v = Vehicle("Toyota", 2020)
c = Car("Toyota", 2023, "Corolla")

v.info()
c.info()
