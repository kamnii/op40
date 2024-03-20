# Принципы ООП - Наследование, Полиморфизм, Инкапсуляция, Абстракция

def w(function):
    def wrapper(*args):
        return function(*args)

    return wrapper()


class A:
    name = 'l'

    def __init__(self, name, radius):
        self.name = name
        self.radius = radius

    def XY(self, x, y):
        self.fine()
        print(x, y)

    def wrong(self):
        print('Привет')


class Rectangle(A):
    def __init__(self, name, radius, color):
        super().__init__(name, radius)
        self.color = color
    name = 'Прямоугольник'

    def wrong(self):
        print(f'Привет {self.name}')

    def vizion(self):
        self.wrong()
        super().wrong()

    def fine(self):
        self.wrong()
        print(self.name)


class Figure(A):
    name = 'Квадрат'

    def vizion(self):
        self.wrong()

    def fine(self):
        print(self.name)


a = A(name='name', radius='100')
a.wrong()

d = Rectangle(name='req', radius='1', color='red')
d.vizion()
