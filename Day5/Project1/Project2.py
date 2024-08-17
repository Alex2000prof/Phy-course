import random
class Game():
    def get_user_item(self):
        while True:
            choice = input("pleasse choose: rock(r)/scissors(s)/paper(p)").strip()
            if choice != "r" and choice != "s" and choice != "p":
                print("invalid choice")
                continue
            else: 
                return choice
    def get_computer_item(self):
        choices = ["r", "s", "p"]
        comp_choice = random.choice(choices)
        return comp_choice
    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        elif (user_item == "r" and computer_item == "s") or \
             (user_item == "s" and computer_item == "p") or \
             (user_item == "p" and computer_item == "r"):
            return "win"
        else:
            return "loss"
    def play(self):   
        user_item = self.get_user_item()
        comp_item = self.get_computer_item()
        result = self.get_game_result(user_item,comp_item)
        if result == "draw":
            print("DRAW")
        elif result == "win":
            print("u a winnner!!!")
        else:
            print("u a loserr:((")

        return result