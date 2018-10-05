"""
ICS 31 Lab 8 Problem 1
Author: UCI_ID: 68168196 Name: Lillian Pham
"""
import random

class Card:
    Name = None
    Value = None

class Bets:
    player_funds = 100
    player_bet = 0

def makeCard(Name: str, Value: int) -> Card:
    c = Card()
    c.Name = Name
    c.Value = Value
    return c

def select_Sort(Card_Deck: [Card]) -> [Card]:
    new_sorted_deck = []
    while len(Card_Deck) > 0:
        min_card = Card_Deck[0]
        min_index = 0
        for check_index in range(len(Card_Deck)):
            if Card_Deck[check_index].Value < min_card.Value:
                min_card = Card_Deck[check_index]
                min_index = check_index
            elif Card_Deck[check_index].Value == min_card.Value:
                if Card_Deck[check_index].Name < min_card.Name:
                    min_card = Card_Deck[check_index]
                    min_index = check_index
        new_sorted_deck.append(min_card)
        del Card_Deck[min_index]
    return new_sorted_deck

def make_Card_Deck_List(my_deck: [{str: int}]) -> [Card]:
    Card_Deck = []
    for key in my_deck:
        Card_Deck.append(makeCard(key, my_deck[key]))
    return Card_Deck

def make_standard_Card_Deck_List(my_deck: {str:int}) -> [Card]:
    list_of_card_objects = make_Card_Deck_List(my_deck)
    new_sorted_deck = select_Sort(list_of_card_objects)
    return new_sorted_deck
    
def print_Deck(card_deck_list: [Card]):
    for c in card_deck_list:
        print(c.Name, ":", c.Value)

def generate_shuffled_deck(full_deck: [Card]) -> [Card]:
    shuffle_list = full_deck.copy() 
    random.shuffle(shuffle_list)
    return shuffle_list

def menu(b: Bets):
    print("You now have $" + b.player_funds)

def intro_message():
    print("Hello and Welcome to the Friend Computer's BlackJack Table!")
    print("At the Friend Computer's BlackJack Tables the closest player to 21, with a value less than 21 wins!")
    print("If you exceed 21, you lose. If the computer has card values closer to 21, you lose.")
    print("If you are closer to 21 than the computer, then you win!")
    print("Note: Ace defaults to 11, but will change to 1, should you exceed 21.")
    print("Also Beware the Friend Computer NEVER turns down a bet and is infinitely wealthy.")
    print("Let's get started.")

def drawCard(available_cards: [Card]) -> Card:
    draw_card = available_cards.pop()
    return draw_card

def createStartingHand(available_cards: [Card], num_to_draw: int) -> [Card]:
    card_list = []
    for i in range(num_to_draw):
        card = drawCard(available_cards)
        card_list.append(card)
    return card_list
        #print(card.Name, str(card.Value))
    #total = eval_Hand(card_list)
    #print("For a total value of:", total)

def print_Hand(card_list: [Card]):
    for c in card_list:
        print(c.Name, ":", c.Value)

def eval_Hand(card_list: [Card]) -> int:
    total = 0
    number_of_aces = 0
    for c in card_list:
        total += c.Value
        if "Ace" in c.Name:
            number_of_aces += 1
    while total > 21 and number_of_aces > 0:
        total -= 10
        number_of_aces -= 1
    return total

def print_player_hand(player_hand: [Card]):
    print_Hand(player_hand)
    total = eval_Hand(player_hand)
    print("For a total value of:", total)

def print_computer_hand(computer_hand: [Card]):
    print_Hand(computer_hand)
    total = eval_Hand(computer_hand)
    print("For a total value of:", total)
    
def getH_or_SChoice() -> str:
    choice = input("Would you like to Hit(H) or Stay(S)? ").strip().upper()
    while choice != "H" and choice != "S":
        print("Invalid choice.")
        choice = input("Would you like to Hit(H) or Stay(S)? ").strip().upper()
    return choice  

def stayOrHit(player_hand: [Card], available_cards: [Card], c: Card) -> bool:
    choice = getH_or_SChoice()
    if choice == "H":
        card = drawCard(available_cards)
        player_hand.append(card)
        print("You drew", card.Name, "which has a value of", card.Value)
        v = eval_Hand(player_hand)
        if v <= 21:
            print("Your hand now has a total value of:", v)
        else:
            print("Oh no!! Your hand has busted as it has exceeded 21")
            return True
    if choice == "S":
        print("You chose to stay/skip your turn.")
        return False

def getBetChoice() -> str:
    choice = input("Would you like to Raise(R) or Stay(S)? ").strip().upper()
    while choice != "R" and choice != "S":
        print("Invalid choice.")
        choice = input("Would you like to Raise(R) or Stay(S)? ").strip().upper()
    return choice 

def getBetAmount(available_for_bet: int) -> int:
    choice = int(input("How much would you like to raise by? "))
    while True:
        if choice <= int(available_for_bet):
            return choice
        elif choice > int(available_for_bet):
            print("Your bet exceeds the available funds. Try again.")
            choice = int(input("How much would you like to raise by? "))
        else:
            print("Invalid bet amount. Try again.")
            choice = int(input("How much would you like to raise by? "))
    return choice
             
def betting(b: Bets, funds: int):
    print("Your current bet is $" + str(b.player_bet)+ " of your $" + str(b.player_funds) + " funds")
    available_for_bet = str(b.player_funds)
    print("You can increase your bet by at most $" + available_for_bet)
    choice = getBetChoice()
    if choice == "R":
        raise_bet = getBetAmount(available_for_bet)
        b.player_bet += raise_bet
        b.player_funds -= raise_bet
        print("Your bet has been increased to $" + str(b.player_bet))
    elif choice == "S":
        print("Your bet is unchanged and remains", str(b.player_bet))
    
def computerTurn(computer_hand: [Card], available_cards: [Card]) -> bool:
    v = eval_Hand(computer_hand)
    if v < 17:
        print("The Friend Computer Hits.")
        computer_hand.append(drawCard(available_cards))
        return True
    return False

def runRound(full_deck: [{str: int}], funds: int, b: Bets, c: Card):
    list_of_card_objects = make_Card_Deck_List(full_deck)
    shuffled = generate_shuffled_deck(list_of_card_objects)
    print("Your hand contains:")
    player_hand = createStartingHand(shuffled, 2)
    print_player_hand(player_hand)
    computer_hand = createStartingHand(shuffled, 2)
    betting(b, funds)
    p = stayOrHit(player_hand, list_of_card_objects, c)
    betting(b, funds)
    cp = computerTurn(computer_hand, list_of_card_objects)
    if p == True:
        return
    elif cp == True:
        return
    elif p == False and cp == False:
        evaluate_player = eval_Hand(player_hand)
        evaluate_comp = eval_Hand(computer_hand)
        print("All players have chosen to stay, so we will reveal hands.")
        print("Your hand had a final value of", evaluate_player)
        print("The Friend Computer had a final value of", evaluate_comp)
        if evaluate_comp > evaluate_player:
            print("The Friend Computer has triumphed!")
            print("The Friend Computer had a better hand this time.")
            print("Your funds have been decreased by your bet size.")
            b.player_funds -= b.player_bet
            print("You now have $" + str(b.player_funds))
        elif evaluate_player > evaluate_comp:
            print("Congrats! Your hand was better than the Friend Computer's!")
            print("Your funds have been increased by your bet size.")
            b.player_funds += b.player_bet
            print("You now have $" + str(b.player_funds))
        return

def getString(prompt: str, options: [str]) -> str:
    choice = input(prompt).strip().upper()
    while not choice in options:
        print("Invalid input.", end = "")
        if len(options) == 2:
            print(options[0], "or", options[1])
        else:
            for option in options:
                if option != options[-1]:
                    print(option, end = ",")
                else:
                    print(" or", options)
        choice = input(prompt).strip().upper()
    return choice

def runGame(full_deck: [{str: int}], Game_Money: int, b: Bets, c: Card):
    intro_message()
    runRound(full_deck, Game_Money, b, c)
    print("The Friend Computer has challenged you to another round!")
    while True:
        prompt = input("Would you like to Continue and Play Another Round(C) or Quit(Q)? ").strip().upper()
        options = ["C", "Q"]
        if prompt not in options:
            prompt = input("Would you like to Continue and Play Another Round(C) or Quit(Q)? ").strip().upper()
        elif prompt == "C":
            runRound(full_deck, Game_Money, b, c)
        elif prompt == "Q":
            break
    
def main():
    b = Bets()
    c = Card()
    full_deck = {
        "Ace of Spades" : 11,
        "Two of Spades" : 2,
        "Three of Spades" : 3,
        "Four of Spades" : 4,
        "Five of Spades" : 5,
        "Six of Spades" : 6,
        "Seven of Spades" : 7,
        "Eight of Spades" : 8,
        "Nine of Spades" : 9,
        "Ten of Spades" : 10,
        "Jack of Spades" : 10,
        "Queen of Spades" : 10,
        "King of Spades" : 10,
        "Ace of Hearts" : 11,
        "Two of Hearts" : 2,
        "Three of Hearts" : 3,
        "Four of Hearts" : 4,
        "Five of Hearts" : 5,
        "Six of Hearts" : 6,
        "Seven of Hearts" : 7,
        "Eight of Hearts" : 8,
        "Nine of Hearts" : 9,
        "Ten of Hearts" : 10,
        "Jack of Hearts" : 10,
        "Queen of Hearts" : 10,
        "King of Hearts" : 10,
        "Ace of Diamonds" : 11,
        "Two of Diamonds" : 2,
        "Three of Diamonds" : 3,
        "Four of Diamonds" : 4,
        "Five of Diamonds" : 5,
        "Six of Diamonds" : 6,
        "Seven of Diamonds" : 7,
        "Eight of Diamonds" : 8,
        "Nine of Diamonds" : 9,
        "Ten of Diamonds" : 10,
        "Jack of Diamonds" : 10,
        "Queen of Diamonds" : 10,
        "King of Diamonds" : 10,
        "Ace of Clubs" : 11,
        "Two of Clubs" : 2,
        "Three of Clubs" : 3,
        "Four of Clubs" : 4,
        "Five of Clubs" : 5,
        "Six of Clubs" : 6,
        "Seven of Clubs" : 7,
        "Eight of Clubs" : 8,
        "Nine of Clubs" : 9,
        "Ten of Clubs" : 10,
        "Jack of Clubs" : 10,
        "Queen of Clubs" : 10,
        "King of Clubs" : 10}
    Game_Money = b.player_funds
    runGame(full_deck, Game_Money, b, c)

if __name__ == "__main__":
	main()
