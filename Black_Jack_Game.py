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
playing = True


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
        while self.value > 21 and self.aces:
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
            if chips.bet > chips.total or chips.bet <= 0:
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
def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop

    while True:
        x = input("would you like to Hit or Stand 'h' or 's' ")

        if x[0].lower() == "h":
            hit(deck, hand)  # Hit function define above
        elif x[0].lower() == "s":
            print("Player stands. Dealer is Playing")
            playing = False

        else:
            print("Sorry, I did not understand that! Please enter 'h' or 's' only!")
            continue
        break


# Step 9:- function to display The Cards


# This function is just gonna be very start of the FACE-OFF
def show_some(player, dealer):

    # dealer.cards[0] --> Hidden
    # show only one of dealer's card
    print("\n Dealer's hand: ")
    print("First Card Hidden")
    print(dealer.cards[1])

    # show all of Player's Cards(2 Cards)
    print("\n Player's Hand: ")
    for card in player.cards:
        print(card)


# This is at the End, where you see who Wins, Lose or if it's a Push
def show_all(player, dealer):
    # show all the Dealer's cards
    print("\n Dealer's Hand: ")
    for card in dealer.cards:
        print(card)

    # calculate and display Value (e.g--> Jack+Queen = 20)
    print(f"Value of the Dealer's hand is: {dealer.value}")

    # show all of Player's Cards(2 Cards)
    print("\n Player's Hand: ")
    for card in player.cards:
        print(card)
    print(f"Value of the Player's hand is: {player.value}")


# Step 10:- function to handle End of the Game Scenarios
def player_busts(player, dealer, chips):
    print("Player Bust!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("Player WINS!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("Dealer Bust!")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("Dealer Wins!")
    chips.lose_bet()


def push(player, dealer):
    print("TIE! PUSH")


# Step 11:- LOGIC OF THE GAME.

while True:
    # Print an opening statement
    print("WELCOME TO bLACKJACK")

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set up the Player's chips
    player_chips = Chips()

    # Prompt the Player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)

    while playing:  # recall this variable from our hit_or_stand function
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)

            # show all cards of the Dealer's hand,
            show_all(player_hand, dealer_hand)

            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        # Show all cards
        show_all(player_hand, dealer_hand)

        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)

    # Inform Player of their chips total
    print(f"\n Player total chips at: {player_chips.total}")
    # Ask to play again
    new_game = input("Would you like to go for an another round y/n? ")

    if new_game[0].lower() == "y":
        playing = True
        continue
    else:
        print("Thanks for playing")

        break
