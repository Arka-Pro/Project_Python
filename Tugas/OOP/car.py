class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def function(self):
        print("gas")

Lembergember = Car("Lamborghini", "Aventador", "2021")
print(Lembergember.make)
print(Lembergember.model)
print(Lembergember.year)
Lembergember.function()