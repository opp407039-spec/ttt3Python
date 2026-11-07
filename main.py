class Human:
    voice = True
    def __init__(self, name, surname, age, height):
        self.name = name
        self.surname = surname
        self.age = age
        self.height = height


denis = Human("Denis", "Andrieiev", 33, 175)
anna = Human("Anna", "Ivanova", 15, 125)

print(denis.name)
print(denis.surname)
print(denis.voice)

print(anna.name)
print(anna.surname)
print(anna.voice)