class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
cat_1 = Cat("Vasya", 10)
cat_2 = Cat("Olya", 7)
cat_3 = Cat("Petya", 14)
def search_old_cat(*cats):
    oldest_cat = cats[0]
    for cat in cats[1:]:
        if cat.age > oldest_cat.age:
            oldest_cat = cat
    return oldest_cat
oldest_cat = search_old_cat(cat_1,cat_2,cat_3)
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")

class Dog:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} goes woof!")
    def jump(self):
        x = self.height*2
        print(f"{self.name}jumps {x} cm high!")
davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Cup",20)
davids_dog.bark()
davids_dog.jump()
sarahs_dog.bark()
sarahs_dog.jump()
if davids_dog.height > sarahs_dog.height:
    big_dog = davids_dog
else:
    big_dog = sarahs_dog
print(f"The biggest dog is: {big_dog.name}")

class Song:
    def __init__(self, lyrics = list()):
        self.lyrics = lyrics 
    def sing_me_a_song(self):
        for word in self.lyrics:
            print(word)
stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()

class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
        else:
            print(f"{new_animal} is already in the zoo.")

    def get_animals(self):
        if self.animals:
            print("Animals in the zoo:")
            for animal in self.animals:
                print(animal)
        else:
            print("No animals in the zoo.")

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
        else:
            print(f"{animal_sold} is not in the zoo.")

    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        sorted_animals_new = {}
        
        for animal in sorted_animals:
            first_letter = animal[0].upper()
            if first_letter not in sorted_animals_new:
                sorted_animals_new[first_letter] = []
            sorted_animals_new[first_letter].append(animal)
        
        return sorted_animals_new

    def get_groups(self):
        sorted_animals_new = self.sort_animals()
        print("Animals grouped by first letter:")
        for letter, animals in sorted_animals_new.items():
            print(f"{letter}: {animals}")
ramat_gan_safari = Zoo("Ramat Gan Safari")
ramat_gan_safari.add_animal("Pantera")
ramat_gan_safari.add_animal("Dog")
ramat_gan_safari.add_animal("Bear")
ramat_gan_safari.add_animal("Cat")
ramat_gan_safari.add_animal("Baboon")
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal("Cat")
ramat_gan_safari.get_animals()
ramat_gan_safari.get_groups()
    
        



        