from HW_Week3_Day2 import Dog
import random
class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name,age,weight)
        self.trained = trained
    def train(self): 
        print(self.bark())
        self.trained = True
    def play(self, *dog_names):
        names = ", ".join(dog_names) + f", {self.name}"
        print(f"{names} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            print(random.choice(tricks))
dog_first = PetDog("Rex", 5, 40)
dog_second = PetDog("Vova", 2, 50)
dog_third = PetDog("Plushka", 9, 20)
dog_first.train()
dog_first.play(dog_second.name, dog_third.name)
dog_first.do_a_trick()

            


