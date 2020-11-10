from random import shuffle

class Blackjack:
    """
    This class creates a command line game of blackjack against the computer (player vs dealer(CPU))
    """
    def __init__(self, buy_in=250):
        """
        Constructor for the Blackjack game

        Args:
            player_purse: Current integer value of player's purse optionally set by passed in argument
            buy_in: Optionally set buy-in value for the player (default 250)
            pot: Integer holding current bet for current round
            master_deck: List of 6x Decks comprising tuples representing cards of tuples (suit, value)
        """

        # Tracker for number of turns
        self.turn_count = 1

        # T/F for if game is active
        self.game_state = True

        # Sets player purse to passed buy_in argument
        self.player_purse = buy_in

        # Creates player_isStand and dealer_isStand both to false
        self.player_isStand = False
        self.dealer_isStand = False

        # Sets dealer_count and player_count to 0, which tracks current quantity of card's value for each hand
        self.player_count = 0
        self.dealer_count = 0

        # Sets pot to be an integer to hold current bet for current round
        self.pot = int

        # Sets the master_deck to a list of 6 individual decks combined
        self.master_deck = list()
        self.master_deck.append(Deck for i in range(0, 6))
        shuffle(self.master_deck)

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

    def game(self):
        # Initial player bet
        self.player_bet()

        # Cards are drawn
        self.player_hand.append(self.draw())
        self.dealer_hand.append(self.draw())
        self.player_hand.append(self.draw())
        self.dealer_hand.append(self.draw())

        while self.game_state is True:
            # If player is not standing, prompt player with dashboard
            if self.player_isStand is False:
                self.player_round()

            # Check if player hand is bust, if so change game state
            if self.player_isBust():
                self.game_state = False

            # TODO: Ensure player_count updates after each hit

            self.dealer_round()
            # Check if dealer hand is bust, if so change game state

            self.turn_count += 1


    def player_round(self):
        """
        Dashboard for player to make actions
        """

        print("Your Turn")

        # Print current hand
        print("\nCurrent hand: ")
        for i in self.player_hand:
            print(f"{self.player_hand[i][2]} of {self.player_hand[i][0]}")
            self.player_count += self.player_hand[i][1]

        print(f"Current Total: {self.player_count}")


        # Print dealer's hand
        print("\nDealer's hand: ")
        for i in self.dealer_hand:
            if i == 0:
                print(f"{self.dealer_hand[i][2]} of {self.dealer_hand[i][0]}")

            print(f"{len(self.dealer_hand) - 1} face-down card(s)")

        # Print betting information
        print(f"\nPot: {self.pot}")
        print(f"Your Purse: {self.player_purse}")

        self.current_action()

    def current_action(self):
        """
        Prints current actions for player
        """

        # Determine player action
        print("\nWhat is your action?")
        print("[1] Hit")
        print("[2] Stand")

        # TODO: Add handling to prompt for a split if the condition is right
        # print("[3] Split")

        if self.turn_count == 1:
            print("[4] Double-down")

        while True:
            print("\nEnter corresponding number below: ")
            player_input = int(input())

            # TODO: Add handling to prompt for a split if the condition is right
            if player_input == 1:
                self.player_hit()
            elif player_input == 2:
                self.player_stand()
            elif player_input == 4 and self.turn_count == 1:
                self.player_double_down()

    def player_bet(self):
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


    def player_hit(self):
        """
        Player hits
        """

        # Calls for player to bet
        self.player_bet()

        # Adds top card from deck to player's hand


        new_card = self.draw()

        # Ace condition check (1 or 11)
        if new_card[1] is 14:
            if (11 + self.player_count) > 21:
                new_card[1] = 1
            else:
                while True:
                    print("\nYou drew an ace. Would you like it to be a 1 or an 11?: ")
                    ace_value = int(input())

                    if ace_value is 1 or 11:
                        new_card[1] = ace_value
                        self.player_hand.append(new_card)
                        continue

                    print("\nInputted value is not a 1 or 11, try again")



    def player_stand(self):
        """
        Sets player_isStand condition to True, passing turns
        """

        self.player_isStand = True



    def player_split(self):


    def player_double_down(self):


    def player_isBust(self):
        """
        Determines if hand is bust for player

        Returns: True if bust, false if not
        """

        return self.player_count > 21

    def dealer_round(self):

        # Assess dealer count
        for i in self.dealer_hand:
            self.dealer_count += self.dealer_hand[i][1]


    def dealer_hit(self):


    def dealer_stand(self):
        """
        Sets dealer_isStand condition to True, passing turns
        """
        self.dealer_isStand = True

    def dealer_isBust(self):
        """
        Determines if hand is bust for dealer

        Returns: True if bust, false if not
        """

        return self.dealer_count > 21




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

            # Reset face card values to 10 except ace which will retain identification as 14
            if self.name != "Ace":
                self.value = 10


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

