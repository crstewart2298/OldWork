class Animal:
    def __init__(self):
        print("in animal initializer")

    def make_noise(self):
        print(self.noise)

    def eat(self, food):
        print('munnchh...muunncchh...')


class Dog(Animal):
    def __init__(self, name, weight, color):
        super().__init__()
        self.name = name
        self.weight = weight
        self.color = color
        self.noise = 'woof'
        print("in dog initializer")

class Frog(Animal):
    def __init__(self, name, weight, color):
        super().__init__()
        self.name = name
        self.weight = weight
        self.color = color
        self.noise = 'ribbit'
        print("in frog initializer")

class Pig(Animal):
    def __init__(self, name, weight, color):
        super().__init__()
        self.name = name
        self.weight = weight
        self.color = color
        self.noise = 'oink'
        print("in pig initializer")

class Squirrel(Animal):
    def __init__(self, name, weight, color):
        super().__init__()
        self.name = name
        self.weight = weight
        self.color = color
        self.noise = 'squeek'
        print("in squirrel initializer")
