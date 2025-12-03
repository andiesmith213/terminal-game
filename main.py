#Pokemon/MTG card game
#Each player is given 5 cards at random that will be their deck
#There will be Attack cards, Spell cards and Defense cards
#The game will go for 3 rounds and each player will get a new, randomly selected card at the end of their turn
#After 3 rounds, the player with the most health wins

#Create a class for the player and classes for each card type
#The player class will contain their name, HP, and deck
#The card classes will contain methods with the modifiers it will place on the player class
#Each card has a type: fire, water, earth or air for attack or defense cards, and type "special" for spell cards
#The element type that is weak against another type will do double damage to that card and half damage if the element is resistant
#Players will also choose an element, that will not be revealed to the other player
#Fire: weak against water, resistant to air
#Water: weak against earth, resistant to fire
#Earth: weak against air, resistant to water
#Air: weak against fire, resistant to earth
#Defense cards will take damage for the player
#Attack cards will do damage to the other player
#The amount of damage the card will reflect or inflict will be an attribute of the card class
#Spell cards will do 1 of 2 things: provide the player with HP or inflict damage to the other player (bypassing any defenders)

#Import libraries
import random as rand

#Declare classes
class Player:
    deck = []

    def __init__(self, name, element):
        self.name = name
        self.health = 100
        self.element = element

    def __repr__(self):
        return "Welcome to the arena, {name}!".format(name=self.name)
    
class Card:
    #This class will be randomized to choose values based off its type
    #It will also be randomly assigned an element
    is_attacking = False

    def __init__(self):
        match rand.randint(1, 4):
            case 1: self.element = "water"
            case 2: self.element = "air"
            case 3: self.element = "fire"
            case 4: self.element = "earth"
        type_select = rand.randint(1, 3)    #1 = attack card, 2 = defense card, 3 = spell card
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

print("Welcome to the Mega Smash card arena!")
print("First, the prompt will ask for your name. Then, you will choose from one of the four elements")
print("Fire\nEarth\nWater\nAir")

#Define first player parameters
player1_name = input("Please enter the name of player 1: ")
player1_element = input("Please enter which element type you'd like to be (p.s. don't let your oponent see) ")
player1 = Player(player1_name, player1_element)
print(player1)

#Define second player parameters
player2_name = input("Please enter the name of player 2: ")
player2_element = input("Please enter which element type you'd like to be (p.s. don't let your oponent see) ")
player2 = Player(player2_name, player2_element)
print(player2)
        
