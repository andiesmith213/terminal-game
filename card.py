  
#This class will be randomized to choose values based off its type
#It will also be randomly assigned an element
import random as rand

class Card:
    def __init__(self):
        type_select = rand.randint(1, 3)    #1 = attack card, 2 = defense card, 3 = spell card  #FIXME the distribution isn't good, figure out better way
        if type_select == 1:
            self.type = "attack"
            self.power = rand.randint(1, 20)
            self.toughness = 0
        if type_select == 2:
            self.type = "defense"
            self.power = 0
            self.toughness = rand.randint(1, 20)
        if type_select == 3:
            self.type = "special"
            self.power = rand.randint(1, 20)
            self.toughness = rand.randint(1, 20)

    def __repr__(self):
        return "This card is a(n) {type} card with {attack} attack and {defense} defense".format(type=self.type, attack=self.power, defense=self.toughness)
    
    def get_card_info(self):
        if self.type == "attack":
            info = "attack card with power = {power}".format(power=self.power)
        elif self.type == "defense":
            info = "defense card with toughness = {toughness}".format(toughness=self.toughness)
        elif self.type == "special":
            info = "special card with attack = {power} and toughness = {toughness}".format(power=self.power, toughness=self.toughness)
        else:
            info = "card info not available"
        return info