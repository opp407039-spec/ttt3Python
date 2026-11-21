class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} видає звук")

    def info(self):
        print(f"Тварина: {self.name}, вік: {self.age}")


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def make_sound(self):
        print(f"{self.name}: Гав-гав!")


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def make_sound(self):
        print(f"{self.name}: Мяу!")


if __name__ == "__main__":
    dog = Dog("Рекс", 3, "Вівчарка")
    cat = Cat("Мурка", 2, "Сірий")
    dog.info()
    dog.make_sound()
    cat.info()
    cat.make_sound()