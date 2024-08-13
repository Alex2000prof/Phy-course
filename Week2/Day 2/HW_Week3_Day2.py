class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f"{self.name} is just walking around"

class Bengal(Cat):
    def sing(self, sounds):
        return f"{sounds}"

class Chartreux(Cat):
    def sing(self, sounds):
        return f"{sounds}"

class Siamese(Cat):
    def sing(self, sounds):
        return f"{sounds}"
bengal_cat = Bengal("vaska", 1)
chartreux_cat = Chartreux("petka", 2)
siamese_cat = Siamese("puska", 3)
all_cats = [bengal_cat,chartreux_cat,siamese_cat]
sara_pets = Pets(all_cats)
sara_pets.walk()

class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        fighter = self.run_speed() * self.weight
        another_fighter = other_dog.run_speed() * other_dog.weight
        if fighter > another_fighter:
            return f"{self.name} wins against {other_dog.name}"
        else:
            return f"{other_dog.name} wins against {self.name}"
dog_first = Dog("Rex", 5, 40)
dog_second = Dog("Vova", 2, 50)
dog_third = Dog("Plushka", 9, 20)
print(dog_first.bark())
print(dog_second.run_speed())
print(dog_third.fight(dog_first))

class Family:
    def __init__(self,last_name, members=None):
        if members is None:
            members  = []
        self.members = members
        self.last_name = last_name 
    def born(self, **kwargs):
        child = {"name": kwargs.get("name"), "age": kwargs.get("age", 0), "gender": kwargs.get("gender", "unknown")}
        self.members.append(child)
        print(f" Congratulations! your family {self.last_name} has new {child["name"]}")
    def is_18 (self, name):
        for member in self.members:
            if member.get("name") == name:
                return member.get("age", 0) >= 18
        return False
    def family_presentation(self):
        print(f"Family: {self.last_name} consist of:")
        for member in self.members:
            print(f" {member["name"]}, {member["age"]} years old, {member["gender"]}, {member["power"]}, {member["incredible_name"]}")
fam = Family("Pribylov")
fam.born(name="Sasha", age=0, gender="male",power="fly",incredible_name="buster")

        
class TheIncredibles(Family):
    def __init__(self, last_name, members=None):
        super().__init__(last_name, members)
    def use_power(self, name):
        member = next((m for m in self.members if m["name"] == name), None)
        if member:
            if member["age"] >= 18:
                print(f"{member['incredible_name']} uses {member['power']}!")
            else:   
                raise Exception(f"{name} is less than 18")
        else:
            print("Not found")
    def incredible_presentation(self):
        print("Here is our powerful family: ")
        super().family_presentation()

in_family = TheIncredibles(
    "Incredibles",
       [
        {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
        {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
    ]
)
in_family.incredible_presentation()
in_family.born(name="Baby Jack", age=0, gender="Male", power="Unknown Power", incredible_name="Baby Jack")
in_family.incredible_presentation()
in_family.use_power("Sarah")








        

        

