from random import shuffle

class Blackjack:
    """
    This class creates a command line game of blackjack against the computer (player vs dealer(CPU))
    """
    def __init__(self, player_purse, player_hand, dealer_hand, pot, master_deck, buy_in=250):
        """
        Constructor for the Blackjack game

        Args:
            player_purse: Current integer value of player's purse optionally set by passed in argument
            buy_in: Optionally set buy-in value for the player (default 250)
            pot: Integer holding current bet for current round
            master_deck: List of 6x Decks comprising tuples representing cards of tuples (suit, value)
        """

        # Sets player purse to passed buy_in argument
        self.player_purse = buy_in

        # Sets pot to be an integer to hold current bet for current round
        self.pot = int

        # Sets the master_deck to a list of 6 individual decks combined
        self.master_deck = list.append(Deck for i in range(0,6))
        shuffle(master_deck)

        # Creates an instance_deck, which is a copy of the master deck to be used in play while preserving master_deck
        self.instance_deck = list(self.master_deck)

        # Sets the player_hand and dealer_hand to lists to hold current cards
        self.player_hand = list()
        self.dealer_hand = list()


    def draw(self):
        """
        Returns: Returns the top card (first card) in the deck
        """
        return self.instance_deck.pop(0)

    def round(self):
        # Initial bet
        self.bet()

        # Cards are drawn
        self.player_hand.append(self.draw())
        self.dealer_hand.append(self.draw())
        self.player_hand.append(self.draw())
        self.dealer_hand.append(self.draw())


    def current_action(self):
        """
        Prints current actions
        """

    def bet(self):
        """
        Player bets
        """
        while True:
            print("\nPlace your bet: $")
            player_bet = int(input())

            if player_bet <= self.player_purse:
                self.pot += player_bet
                self.player_purse -= player_bet
                continue

            print("\nBet exceeds current purse, try again")


    def hit(self):


    def stand(self):


    def fold(self):


    def split(self):


    def double_down(self):

class Card:
    """
    This class makes a single card, with suit and value
    """
    def __init__(self, value, suit):
        """
        Constructor for card

        Args:
            value: (int) value of card
            suit: (str) suit of card
            name: (str) name of card (2, king, ...)
        """
        self.suit = suit
        self.value = value

        names = {11:"Jack", 12:"Queen", 13:"King", 14:"Ace"}

        if 2 <= value <= 10:
            self.name = str(value)
        else:
            self.name = names[value]

class Deck:
    """
    This is a deck of cards, as a list of tuples (suit, value, name)
    """
        
    def __init__(self):
        """
        Constructor of the deck, creates 52 standard playing cards and shuffles them
        """
        self.cards = list()

        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

        for i in range(len(suits)):
            for j in range(2, 15):
                self.cards.append(Card(j, suits[i]))

        shuffle(self.cards)

