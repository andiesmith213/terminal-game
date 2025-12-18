#Pokemon/MTG card game
#Each player is given 5 cards at random that will be their deck
#There will be Attack cards, Spell cards and Defense cards
#The game will go for 5 rounds and each player will get a new, randomly selected card at the end of their turn
#After the rounds end, the player with the most health wins

#Create a class for the player and classes for each card type
#The player class will contain their name, HP, and deck
#The card classes will contain methods with the modifiers it will place on the player class
#Defense cards will take damage for the player
#Attack cards will do damage to the other player
#The amount of damage the card will reflect or inflict will be an attribute of the card class
#Spell cards will allow the player to choose from a variety of options. These cards will do 1 of 2 things: attack the other player or add defenders to the player

#FIXME: improve randomization, not well distributed right now
#Extensibility: allow the players to choose how many rounds they want to play instead of setting a hard limit, allowing more than 2 players, and expanding special card options (provide the player with HP)

#Import libraries
from player import Player
from card import Card

def report_player_stats(attacking_player, defending_player):
    print(attacking_player.name + "'s stats:")
    print("\tHealth: " + str(attacking_player.get_player_health()))
    print("\tDefense: " + str(attacking_player.get_defense()))
    
    print(defending_player.name + "'s stats:")
    print("\tHealth: " + str(defending_player.get_player_health()))
    print("\tDefense: " + str(defending_player.get_defense()))

#Returns the value of the player's defense following an attack
def determine_damage(defender, damage):
    #Return defense information to player
    if defender.get_defense() <= 0:
        print(defender.name + " has no defenders")
    else:
        print(defender.name + " has defenders")

    #Calculate new defense value after damage
    defender.reduce_defense(damage)
    damage_overflow = 0
    #Set defender's defense = to calculated defense and return value
    #If more points of damage than defense, the overflow damage impacts the player
    if defender.get_defense() < 0:
        damage_overflow = abs(defender.get_defense())
        defender.set_defense(0)
    return damage_overflow

def battle(card, attacking_player, defending_player):
    #Determine if special card first to know which functions to use
    if card.type == "special":
        print("KABOOM!\n")
        #Clear chosen option from previous round
        attack_or_defend = 0
        #Special cards can act as either defenders or attackers
        #User needs to pick which stat to add to
        print("Would you like to add the special card to your attack stat or your defense stat?")
        #Continue to ask the player until they submit a valid input
        while True:
            attack_or_defend = int(input("Input 1 for attack and 2 for defense "))
            if attack_or_defend == 1 or attack_or_defend == 2:
                break
            else:
                print("Invalid value. Please choose 1 for attack or 2 for defense ")
    if card.type == "attack" or (card.type == "special" and attack_or_defend == 1):
        print("\nPOW!\n")
        print(attacking_player.name + " attacked " + defending_player.name)
        #Attack card inflicts damage on opponent
        #if opponent has defenders, they will take damage first
        damage = card.power
        player_damage = determine_damage(defending_player, damage)
        defending_player.reduce_player_health(player_damage)
        print(defending_player.name + " has taken " + str(player_damage) + " point(s) of damage")
    if card.type == "defense" or (card.type == "special" and attack_or_defend == 2):
        print("\nBAM!\n")
        print(attacking_player.name + " has added defense points to their stats")
        #A defense cards stats should be added to the defense of the active player
        attacking_player.add_defense(card.toughness)
    print("\nEnd of round\n")
    report_player_stats(attacking_player, defending_player)



#Main function
print("Welcome to the Mega Smash card arena!")

#Define first player parameters
# player1_name = input("Please enter the name of player 1: ")
players = 1
player1 = Player("Riddles", players) 

#Define second player parameters
# player2_name = input("Please enter the name of player 2: ")
players += 1
player2 = Player("Bean", players)
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

print("Let's begin!")
for round in range(1, 10):
    print("Round {round}".format(round=round))
    #Determine who's turn it is based off the round being even or odd
    if round % 2 == 0:
        print("{player}'s turn!".format(player=player2.name))
        #Provide player with their deck information and have them choose their card
        card = player2.get_card_deck()
        #Card class now stored in card variable, now choose which function to call based off card type
        #Battle function will return the updated player classes?
        battle(card, player2, player1)
    else:
        print("{player}'s turn!".format(player=player1.name))
        #Provide player with their deck information and have them choose their card
        card = player1.get_card_deck()
        #Card class now stored in card variable, now choose which function to call based off card type
        #Battle function will return the updated player classes?
        battle(card, player1, player2)
