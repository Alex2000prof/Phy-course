class Person:
    num_of_people = 0
    def __init__(self, name):
        self.name = name
        Person.num_of_people += 1
bob = Person("Bob")
alice = Person("Alice")

class Man(Person):
    sex = "Male"

    @staticmethod
    def get_nicknames():
        return ["Bro", "Dude", "Buddy"]