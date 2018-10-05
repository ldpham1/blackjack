import unittest
#from mock import patch
from Blackjack import *

'''
Please use the following structure for automated testing and follow the structure guide.
Use the following class structure and functions which will help you write the program.

To run the test cases just place this file in the same folder as your solution named 
Blackjack.py and run it. The test cases will tell you how many functions are incorrect.

class Card:
    Name   = None 		# Must be one of the keys from the official_deck dictionary
    Value  = None		# Must be one of the values from the official_deck dictionary corresponding to the name

class Bets:
    player_funds    = 0		#Amount of funds available with the player
    player_bet      = 0		

def makeCard(name:str, value:int) -> Card:
	This function accepts the name and value of the card and returns the constructed Card object with the name and value
	assigned to the values passed on to the function.

def select_Sort(Card_Deck:[Card]) -> [Card]:
	This function takes in a list of Card objects, sorts the list and returns the sorted list.

def make_Card_Deck_List(my_deck:[{str:int}]) -> [Card]:
	This function takes in a dictionary of card name and value pairs, creates a list of Card objects and returns it

def make_standard_Card_Deck_List(my_deck:[{card_name:value}]) -> [Card]:
	This function takes in a dictionary of card name and value pairs, creates a list of Card objects, sorts it and returns it

def print_Deck(card_deck_list:[Card]):
	This function takes in as input the list of Card objects and prints the name and value of each card in the list

def generate_shuffled_deck(full_deck:[Card]) -> [Card]:
	This function takes in as input the list of Card objects, shuffles them
	and returns the shuffled list.

def menu():
	This function prints the available funds with the player

def intro_message():
	This function prints the intro message when the game is run for the first time

def drawCard(available_cards:[Card]) -> Card:
	This function returns the last most Card in the list that is given as input and returns the Card

def createStartingHand(available_cards:[Card], num_to_draw:int) -> [Card]:
	This function takes in as input the list of available cards, the number of cards to draw and returns the list 
	of num_of_draw cards.

def print_Hand(card_list:[Card]):
	This function takes in a list of Card objects as input and prints the name and value of each card

def eval_Hand(card_list:[Card]) -> int:
	This function takes in a list of Card objects and returns the total value of all the cards in the list						

def print_player_hand(player_hand:[Card]):
	This function takes in as input the list of Card objects and prints the name, value of each card along with the
	value of all the cards in the list

def print_computer_hand(computer_hand:[Card]):
	This function takes in as input the list of Card objects and prints the name, value of each card along with the
	value of all the cards in the list

def getH_or_SChoice() -> str:
	This function asks the user whether he wants to Hit and Miss, takes in the character input by the user, checks if it 
	is valid. If it is valid, it returns it else it keeps asking the user to enter a valid character.

def stayOrHit(player_hand:[Card], available_cards:[Card]) -> bool:
	This function calls the getH_or_SChoice() function, gets the input entered by the user, if the user entered a 'H', draws 
	an extra card for the player and evaluates it to be a bust or not. 

def getBetChoice() -> str:
	This function asks the user whether he would want to Raise(R) or Stay(S). This function returns the character if it is valid, else
	keeps asking the user to enter a valid input

def getBetAmount(available_for_bet:int) -> int:
	This function asks the user the amount he would like to bet by, checks if it is a valid bet amount and returns it

def betting(funds:int):
	This function prints the current bet amount of the player, gets the Bet choice by calling the getBetChoice() function
	and increases the player bet amount if he chooses to Raise.

def computerTurn(computer_hand:[Card], available_cards:[Card]) -> bool:
	This function evaluates the hand of the computer, if it is less than 17 it hits else stays

def runRound(full_deck:[{str:int}], funds:int):
	This is the function that runs the game by executing the rounds

def getString(prompt:str, options:[str]) -> str:
	This function askes the user a prompt, gets the input made by the user, checks if it is in the options and returns it

def runGame(full_deck:[{str:int}], Game_Money:int):
	This function runs the game by calling in runRound()

def main():
	This sets the seed for random and runs the game			



You are free to add more helper functions but you should code the above mentioned functions in the above mentioned format.

'''

class testFunctions(unittest.TestCase):

	def test_makeCard(self):
		card = makeCard("Two of Spades" , 2)
		self.assertEqual(card.Name, "Two of Spades")
		self.assertEqual(card.Value, 2)
	
	def test_select_Sort(self):
		card2 = makeCard("Nine of Diamonds", 9)
		card1 = makeCard("Ten of Diamonds" , 10)
		list1 = [card1,card2]
		sort_list = select_Sort(list1)
		self.assertEqual(sort_list, [card2,card1])

	def test_make_standard_Card_Deck_List(self):
		res = make_standard_Card_Deck_List({"Ace of Hearts" : 11, "Two of Hearts" : 2})
		self.assertEqual(res[0].Name, "Two of Hearts")
		self.assertEqual(res[0].Value, 2)
		self.assertEqual(res[1].Name, "Ace of Hearts")
		self.assertEqual(res[1].Value, 11)
		
	
	def test_drawCard(self):
		card2 = makeCard("Nine of Diamonds", 9)
		card1 = makeCard("Ten of Diamonds" , 10)
		temp = drawCard([card1, card2])
		self.assertEqual(isinstance(temp, Card),True)
		self.assertEqual(temp.Name,"Nine of Diamonds")
		self.assertEqual(temp.Value, 9)

	def test_createStartingHand(self):
		card2 = makeCard("Nine of Diamonds", 9)
		card1 = makeCard("Ten of Diamonds" , 10)
		temp = createStartingHand([card1,card2], 1)
		self.assertEqual(temp[0].Name,"Nine of Diamonds")
		self.assertEqual(temp[0].Value, 9)	

	def test_eval_Hand(self):
		card2 = makeCard("Nine of Diamonds", 9)
		card3 = makeCard("Nine of Diamonds", 9)
		card1 = makeCard("Eight of Hearts" , 8)
		self.assertEqual(eval_Hand([card1,card2]),17)
		card2 = makeCard("Ace of Spades",11)
		self.assertEqual(eval_Hand([card1,card2,card3]),18)
		
	def test_getH_or_SChoice(self):
		__builtins__.input = lambda _: 'H'
		self.assertEqual(getH_or_SChoice(),'H')
		__builtins__.input = lambda _: 'h  '
		self.assertEqual(getH_or_SChoice(),'H')

	def test_getBetChoice(self):
		__builtins__.input = lambda _: 'R'
		self.assertEqual(getBetChoice(),'R')
		__builtins__.input = lambda _: 's  '
		self.assertEqual(getBetChoice(),'S')

	def test_getBetAmount(self):
		__builtins__.input = lambda _: 20
		self.assertEqual(getBetAmount(30),20)

	def test_computerTurn(self):
		card1 = makeCard("Ace of Hearts" , 11)
		card2 = makeCard("Two of Hearts" , 2)
		card3 = makeCard("Three of Hearts" , 3)
		self.assertEqual(computerTurn([card1,card2], [card3]), True)	


if __name__ == '__main__':
    unittest.main()
