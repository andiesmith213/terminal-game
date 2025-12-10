
class Player:
    def __init__(self, name, element):
        self.name = name
        self.health = 100
        self.element = element

    def __repr__(self):
        return "Welcome to the arena, {name}!".format(name=self.name)
        
    def set_card_deck(self, deck):
        self.deck = deck
    
    def get_card_deck(self):
        print("Here are your available cards:")
        for card in range(len(self.deck)):
            print("{card}. {info}".format(card=card+1, info=self.deck[card].get_card_info()))
        card_value = int(input("Input the card number you want to use ")) - 1        #need to select the index with a starting value of 0
        card_info = self.deck.pop(card_value)
        return card_info