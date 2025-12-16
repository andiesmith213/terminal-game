
class Player:
    def __init__(self, name, player_number):
        self.name = name
        self.health = 100
        self.defense = 0
        self.attack = 0
        self.player_id = player_number

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
    
    def get_player_health(self):
        return self.health
    
    def set_player_health(self, value):
        self.health -= value
    
    def set_defense(self, toughness):
        self.defense += toughness
    
    def get_defense(self):
        return self.defense

    def set_attack(self, attack):
        self.attack += attack

    def get_attack(self):
        return self.attack
    
    def get_player_id(self):
        return self.player_id