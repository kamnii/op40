class Car:
    fars = "True"


    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color



    def Fars(self):
        print(self.fars)


    def __str__(self):
        return f'model: {self.model},\nyear: {self.year},\ncolor: {self.color}'


    def __len__(self):
        return len(self.fars) * 2


car = Car("Ford", 2000, 'red')
car2 = Car("Toyota", 2002, 'white')
car3 = Car('BMW', 2019, 'green')

print(car2)
