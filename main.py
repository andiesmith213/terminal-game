#Pokemon/MTG card game
#Each player is given 5 cards at random that will be their deck
#There will be Attack cards, Spell cards and Defense cards
#The game will go for 5 rounds and each player will get a new, randomly selected card at the end of their turn
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
    
class Card:
    #This class will be randomized to choose values based off its type
    #It will also be randomly assigned an element
    #Declare class variables
    is_attacking = False

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

#Main function
print("Welcome to the Mega Smash card arena!")
print("First, the prompt will ask for your name. Then, you will choose from one of the four elements to embody")
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

#Create player's decks
print("Now, you will be assigned 5 cards to battle with.")
deck1 = []
deck2 = []
#Randomly choose and append 5 cards to each players deck
for index in range(5):
    deck1.append(Card())
    deck2.append(Card())
player1.set_card_deck(deck1)
player2.set_card_deck(deck2)

round = 1
print("Let's begin!\nRound {round}".format(round=round))
print("{player}'s turn!".format(player=player1.name))
#Provide player with their deck information and have them choose their card
card = player1.get_card_deck()
#Card class now stored in card variable, now choose which function to call based off card type

