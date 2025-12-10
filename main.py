#Pokemon/MTG card game
#Each player is given 5 cards at random that will be their deck
#There will be Attack cards, Spell cards and Defense cards
#The game will go for 5 rounds and each player will get a new, randomly selected card at the end of their turn
#After 3 rounds, the player with the most health wins

#Create a class for the player and classes for each card type
#The player class will contain their name, HP, and deck
#The card classes will contain methods with the modifiers it will place on the player class
#TODO elements will be an extensibility feature, get base game working first
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
from player import Player
from card import Card


def battle(card):
    if card.type == "attack":
        pass
    if card.type == "defense":
        pass
    if card.type == "special":
        pass


#Main function
print("Welcome to the Mega Smash card arena!")
print("First, the prompt will ask for your name. Then, you will choose from one of the four elements to embody")
print("Fire\nEarth\nWater\nAir")

#Define first player parameters
#FIXME commenting out to bypass input for testing purposes
# player1_name = input("Please enter the name of player 1: ")
# player1_element = input("Please enter which element type you'd like to be (p.s. don't let your oponent see) ")
# player1 = Player(player1_name, player1_element)     
player1 = Player("Andie", "water")     
print(player1)

#Define second player parameters
#FIXME commenting out to bypass input for testing purposes
# player2_name = input("Please enter the name of player 2: ")
# player2_element = input("Please enter which element type you'd like to be (p.s. don't let your oponent see) ")
# player2 = Player(player2_name, player2_element)
player2 = Player("Ridley", "earth")
print(player2)

#Create player's decks
#FIXME commenting out to bypass input for testing purposes
print("Now, you will be assigned 5 cards to battle with.")
# print(player1.name)
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
battle(card)
