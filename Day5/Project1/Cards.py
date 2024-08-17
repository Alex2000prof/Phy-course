import random
class Cards:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    def __init__(self):
        self.all_cards = []
        for suit in self.suits:
            for value in self.values:
                self.all_cards.append({"value": value, "suit": suit})
    def print_cards(self):
        for card in self.all_cards:
            print(f"{card['value']} of {card['suit']}")
cards = Cards()
cards.print_cards()

#sorry i can try it later i have no energy 

            
