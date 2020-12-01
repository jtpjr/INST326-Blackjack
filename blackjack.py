from random import shuffle

class Deck:
    """
    This is a deck of cards, as a list of tuples (suit, value, name)
    """

    def __init__(self):
        """
        Constructor of the deck, creates 52 standard playing cards and shuffles them.
        First, it initializes the cards attribute to an empty list.  Then, it assigns suits to the list of suits
        and names to a dictionary called names with values (keys) and face card names (values).
        Lastly, we populate the deck of cards by using a nested for loop.
        """
        self.cards = list()

        suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        names = {11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}

        for i in range(0, 4):
            for j in range(2, 15):
                if 2 <= j <= 10:
                    self.cards.append((str(suits[i]), int(j), str(j)))
                elif 10 < j < 15:
                    self.cards.append((str(suits[i]), int(10), str(names[j])))
                else:
                    self.cards.append((str(suits[i]), 14, str(names[j])))

        shuffle(self.cards)

    def get_cards(self):
        """
        Returns: List of cards
        """

        return self.cards


class Blackjack:
    """
    This class creates a command line game of blackjack against the computer (player vs dealer(CPU))
    """
    def __init__(self, buy_in=250):
        """
        Constructor for the Blackjack game

        Args:
            buy_in: How much currency the player is entering the game with
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
        self.pot = int()

        # Sets the master_deck to a list of 6 individual decks combined
        self.master_deck = list()

        for i in range(0, 6):
            for card in Deck().get_cards():
                self.master_deck.append(card)

        # Creates an instance_deck, which is a copy of the master deck to be used in play while preserving master_deck
        self.instance_deck = list()

        for i in self.master_deck:
            self.instance_deck.append(i)

        # Sets the player_hand and dealer_hand to lists to hold current cards
        self.player_hand = list()
        self.dealer_hand = list()


    def draw(self):
        """
        Draws the first card in the deck

        Returns: Returns the top card (first card) in the deck
        """
        return self.instance_deck.pop(0)

    def game(self):
        """
        Structure of the game of blackjack itself
        """
        # Initial player bet
        self.player_bet()

        # Cards are drawn

        #TODO: Add ace handling (Choose for player, pick for cpu)
        #TODO: Add count 21 handling for when blackjack is achieved (set hold status to true automatically in both dealer and player control structures)
        self.player_hand.append(self.draw())
        self.dealer_hand.append(self.draw())
        self.player_hand.append(self.draw())
        self.dealer_hand.append(self.draw())

        while True:
            while self.game_state is True:
                # If player is not standing, prompt player with dashboard
                if self.player_isStand is False and self.player_isBust() is False:
                    self.player_round()

                # Check if player hand is bust, if so change game state
                if self.player_isBust():
                    self.game_state = False

                # TODO: Ensure player_count updates after each hit

                # If dealer is not standing, run dealer round
                if self.dealer_isStand is False and self.dealer_isBust() is False:
                    self.dealer_round()

                # Check if dealer hand is bust, if so change game state
                if self.dealer_isBust():
                    self.game_state = False


                self.turn_count += 1

            while self.game_state is False:
                if self.player_isBust():
                    print("\nDealer wins")
                    self.pot = 0
                    break
                else:
                    print("\nPlayer wins")
                    self.player_purse += self.pot
                    self.pot = 0
                    break


            print("\nPlay again? (y/n)")
            player_input = str(input())

            if player_input == "y" or "Y":
                # Reset all values to defaults
                self.game_state = True
                self.player_hand = list()
                self.dealer_hand = list()
                self.turn_count = 1
                self.player_isStand = False
                self.dealer_isStand = False
                self.player_count = 0
                self.dealer_count = 0
                self.instance_deck = list()

                for i in self.master_deck:
                    self.instance_deck.append(i)
                continue
            elif player_input == "n" or "N":
                quit()

            print("\nInputted value is not a y or n, try again")



    def player_round(self):
        """
        Dashboard for player to make actions
        """

        print("\nYour Turn")

        # Print current hand
        print("\nCurrent hand: ")
        self.player_count = 0

        for i in range(0, len(self.player_hand)):
            print(f"{self.player_hand[i][2]} of {self.player_hand[i][0]}")
            self.player_count += self.player_hand[i][1]

        print(f"Current Total: {self.player_count}")


        # Print dealer's hand
        print("\nDealer's hand: ")
        for i in range(0, len(self.dealer_hand)):
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
                break
            elif player_input == 2:
                self.player_stand()
                break
            elif player_input == 4 and self.turn_count == 1:
                self.player_double_down()
                break

    def player_bet(self):
        """
        The player places their bets for that round.
        If they want to partake in this round they will place their monetary bets
        and after that they cannot take it back.

        Returns: N/A
        """
        while True:
            print("Place your bet: $")
            player_bet = int(input())

            if player_bet <= self.player_purse:
                self.pot += player_bet
                self.player_purse -= player_bet
                return

            print("\nBet exceeds current purse, try again")


    def player_hit(self):
        """
        Player hits, which is to draw a card from the deck and add it to their current hand
        in an attempt to get as close to 21 as possible.
        If they player recieves an ace card on their hit,
        they decide if they want it as a 1 or 11 if mathematically possible,
        given the other cards in their hand.

        Returns: N/A
        """

        # Calls for player to bet
        self.player_bet()

        # Adds top card from deck to player's hand
        new_card = self.draw()

        # Ace condition check (1 or 11)
        if new_card[1] == 14:
            if (11 + self.player_count) > 21:
                new_card = (new_card[0], 1, new_card[2])
            else:
                while True:
                    print("\nYou drew an ace. Would you like it to be a 1 or an 11?: ")
                    ace_value = int(input())

                    if ace_value == 1 or ace_value == 11:
                        new_card = (new_card[0], ace_value, new_card[2])
                        continue

                    print("\nInputted value is not a 1 or 11, try again")

        print(f"You drew a {new_card[2]} of {new_card[0]}")
        self.player_hand.append(new_card)



    def player_stand(self):
        """
        Sets player_isStand condition to True, passing turns
        When a player stands they are staying where they are for the
        round and do not want to take any more cards in hopes of being
        closer to 21 than the dealer.

        Returns: N/A
        """

        self.player_isStand = True



    def player_split(self):
        """
        Handling to allow the player to split current hand in two,
        and play both hands concurrently

        Returns: N/A
        """
        pass


    def player_double_down(self):
        """
        Handling to allow the player to double down during the initial round.
        Doubling down is a chance for the player to
        increase the value of your initial bet by up to 100 per cent.
        You can only double down on your initial turn and it doubles your bet.

        Returns:
        """
        pass


    def player_isBust(self):
        """
        Determines if hand is bust for player.
        A "bust hand" means that you went over 21 points
        and your hand was of no value at all and you lose.

        Returns: Returns true if players hand is busted and false if not.
        """

        return self.player_count > 21

    def dealer_round(self):
        """
        Structured instructions for the dealer's hand.
        Manages the CPU's decision making for competing against the player in game.
        The computer/dealer is given the same options as the one playing the game.
        They decide to get more cards or to stay where they are in an attempt to get
        closer to 21 than the player.

        Returns: NaN
        """

        print("\nDealer's Turn")

        # Checks if first 2 cards received are Aces, and if so, set to 11 value
        for i in range(0, len(self.dealer_hand)):
            if self.dealer_hand[i][1] == 14:
                self.dealer_hand[i][1] = 11

        # Assess dealer count
        for i in range(0, len(self.dealer_hand)):
            self.dealer_count += self.dealer_hand[i][1]

        # Rules: https://blog.udemy.com/blackjack-rules-2/

        if self.dealer_count < 16:
            self.dealer_hit()

            if self.dealer_hand[len(self.dealer_hand)-1][1] == 14:
                self.dealer_hand[len(self.dealer_hand)-1][1] = 11
            return

        if self.dealer_count >= 17:

            # If total is over 21, check for aces and change value from 11 to 1
            if self.dealer_count > 21:
                for i in range(0, len(self.dealer_hand)):
                    if self.dealer_hand[i][1] == 11:
                        self.dealer_hand[i][1] = 1

            return


    def dealer_hit(self):
        """
        Dealer hits, which is to draw a card from the deck and add it to current hand.

        Return: N/A
        """
        # Adds top card from deck to dealer's hand
        print("Dealer hits")

        new_card = self.draw()
        self.dealer_hand.append(new_card)



    def dealer_stand(self):
        """
        Sets dealer_isStand condition to True, passing turns
        When a dealer stands they are staying where they are for the
        round and do not want to take any more cards in hopes of being
        closer to 21 than the player.
        """
        print("Dealer stands")

        self.dealer_isStand = True

    def dealer_isBust(self):
        """
        Determines if hand is bust for dealer.
        A "bust hand" means that you went over 21 points
        and your hand was of no value at all and you lose.

        Returns: Returns true if dealers hand is busted and false if not.
        """
        print("Dealer busts")

        return self.dealer_count > 21


class Blackjack_Test:

    if __name__ == '__main__':
        new_game = Blackjack()

        new_game.game()


