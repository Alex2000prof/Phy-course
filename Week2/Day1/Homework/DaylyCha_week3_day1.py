class Farm:
    def __init__(self,name):
        self.name = name
        self.count_animals = {}
    def add_animal(self,animal,count=1):
        if animal in self.count_animals:
            self.count_animals[animal] += count
        else:
            self.count_animals[animal] = count
    def get_info(self):
        info = f"{self.name}'s farm\n\n"
        for animal, count in self.count_animals.items():
            info += f"{animal} : {count}\n"
        info += "\n    E-I-E-I-0!"
        return info
macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())

        