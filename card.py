  
#This class will be randomized to choose values based off its type
#It will also be randomly assigned an element
import random as rand

class Card:
    def __init__(self):
        match rand.randint(1, 4):
            case 1: self.element = "water"
            case 2: self.element = "air"
            case 3: self.element = "fire"
            case 4: self.element = "earth"
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
        return "This card is a(n) {type} card of the element {element} with {attack} attack and {defense} defense".format(type=self.type, element=self.element, attack=self.power, defense=self.toughness)
    
    def get_card_info(self):
        if self.type == "attack":
            info = "attack {element} card with power = {power}".format(element=self.element, power=self.power)
        elif self.type == "defense":
            info = "defense {element} card with toughness = {toughness}".format(element=self.element, toughness=self.toughness)
        elif self.type == "special":
            info = "special {element} card with attack = {power} and toughness = {toughness}".format(element=self.element, power=self.power, toughness=self.toughness)
        else:
            info = "card info not available"
        return info