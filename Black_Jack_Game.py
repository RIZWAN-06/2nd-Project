# Game Play
# To play a hand of Blackjack the following steps must be followed:
# 1. Create a deck of 52 cards
# 2. Shuffle the deck
# 3. Ask the Player for their bet
# 4. Make sure that the Player's bet does not exceed their available chips
# 5. Deal two cards to the Dealer and two cards to the Player
# 6. Show only one of the Dealer's cards, the other remains hidden
# 7. Show both of the Player's cards
# 8. Ask the Player if they wish to Hit, and take another card
# 9. If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
# 10. If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
# 11. Determine the winner and adjust the Player's chips accordingly
# 12. Ask the Player if they'd like to play again


# Step 1:-

# setting Global variable
import random

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = (
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Jack",
    "Queen",
    "King",
    "Ace",
)
values = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11,
}

# Boolean value to be used for controlling the While Loop
Playing = True


# Step 2:-
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit


# Setp 3:-
class Deck:
    def __init__(self):
        # start with an empty list
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp += "\n" + card.__str__()
        return "The deck has: " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    # To grab the card from my self.deck attribute, that list of card objects
    def deal(self):
        single_card = self.deck.pop()
        return single_card


# Step 4: Create a Hand class


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self, card):
        # card passed in
        # from Deck.deal() --> single Caed(suit, rank)
        self.cards.append(card)
        self.value += values[card.rank]

        # tracking Aces
        if card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):

        # if total value of Ace > 21 and i still have Ace
        # then change my Ace to be 1 instead of 11.
        while self.aces > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


# Step 5:- Create a Chips class
class Chips:
    def __init__(self):

        # This can be set to a default value or supplied by a user input
        self.total = 100

        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


# Step 6:- function for taking bets.
def take_bet(chips):

    while True:
        try:
            chips.bet = int(input("How many Chips would you like to bet?"))
        except:
            print("Sorry please provide an Integer")
        else:
            if chips.bet > chips.total:
                print(f"Sorry! You don't have enough Chips! You have {chips.total}")
            else:
                break


# Step 7:- function for taking hits
def hit(deck, hand):

    # It takes the deck and someone's hand
    # grabs  single card from the deck adds it to the hand
    hand.add_card(deck.deal())

    # then checks for an ace adjustment
    hand.adjust_for_ace()


# Step 8:- function for prompting the Player to Hit or Stand
