from random import shuffle

class Deck:
    """
    This is a deck of playing cards, as a list of tuples (suit, value, name)
    """

    def __init__(self):
        """
        Constructor of the deck, creates 52 standard playing cards and shuffles them.
        First, it initializes the cards attribute to an empty list.  Then, it assigns suits to the list of suits
        and names to a dictionary called names with values (keys) and face card names (values).
        Lastly, we populate the deck of cards by using a nested for loop.

        Returns: N/A
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
        Getter for the list of cards as tuples (suit, value, name) for a standard set of playing cards.

        Returns: List of cards
        """

        return self.cards


class Blackjack:
    """
    This class creates a command line game of blackjack against the computer (player vs dealer(CPU)). This class utilizes
    the Deck class above to populate the deck of cards used in the game. The computer uses an algorithm to determine
    which actions to take against the player, and the player can make the standard array of actions as per the rules
    of blackjack.
    """
    def __init__(self, buy_in=250):
        """
        Constructor for the Blackjack game. Creates a multitude of variables for tracking various gamestates, as well as
        tracking the player and CPU's hands and bets.

        Args:
            buy_in: How much currency the player is entering the game with

        Returns: N/A
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

        # Variable for if player has split
        self.player_isSplit = False
        self.player_secondHand = list()
        self.player_secondCount = 0
        self.player_secondStand = False

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
        Draws the first card in the deck, from the Instance deck created in the constructor.

        Returns: Returns the top card (first card) in the deck as a tuple (suit, value, name)
        """
        return self.instance_deck.pop(0)

    def game(self):
        """
        Structure of the game of blackjack itself. Runs a looped game with constant resetting of variables, and
        contiguous pot/purse tracking to ensure continuity between continued games. Prompts player at the end of each
        game to quit.

        Returns: N/A
        """
        # Initial player bet
        self.player_bet()

        #TODO: Add count 21 handling for when blackjack is achieved (set hold status to true automatically in both dealer and player control structures)

        while True:
            # Cards are drawn
            for i in range(0, 2):
                player_card = self.draw()
                if player_card[2] == "Ace":
                    print("\nYou drew an ace. Would you like it to be a 1 or 11?")
                    while True:
                        player_input = int(input())

                        if player_input == 1 or player_input == 11:
                            player_card = (player_card[0], player_input, player_card[2])
                            break

                        print("Input invalid, please try again")

                self.player_hand.append(player_card)

                self.dealer_hand.append(self.draw())

            while self.game_state is True:
                # If player is not standing, prompt player with dashboard
                if self.player_isStand is False and self.player_isBust() is False and self.game_state is True:
                    print("\nYour Turn")
                    self.player_round()

                # Check if player hand is bust, if so change game state
                if self.player_isBust():
                    self.game_state = False

                # If dealer is not standing, run dealer round
                if self.dealer_isStand is False and self.dealer_isBust() is False and self.game_state is True:
                    print("\nDealer's Turn")
                    self.dealer_round()

                # Check if dealer hand is bust, if so change game state
                if self.dealer_isBust():
                    self.game_state = False

                # Check if both players are holding
                if self.player_isStand is True and self.dealer_isStand is True:
                    self.game_state = False

                self.turn_count += 1

            # Victory evaluation
            while self.game_state is False:
                if self.player_isSplit is False:
                    if self.player_count == self.dealer_count and self.player_count < 21:
                        print("Tie, pot is split")
                        self.player_purse += (self.pot / 2)
                        self.pot = 0
                        break
                    elif self.player_isBust() or 21 >= self.dealer_count > self.player_count:
                        if self.player_isBust():
                            print("Player busts")
                        else:
                            print("Dealer's hand has higher value than player's hand")

                        print("\nDealer wins")
                        self.pot = 0
                        break
                    else:
                        if self.dealer_isBust():
                            print("Dealer busts")
                        else:
                            print("Player's hand has higher value than dealer's hand")

                        print("\nPlayer wins")
                        self.player_purse += (2 * self.pot)
                        self.pot = 0
                        break
                else:
                    if self.dealer_count == self.player_count == self.player_secondStand:
                        print("All hands tie, pot is split")
                        self.player_purse += (self.pot / 2)
                        self.pot = 0
                        break
                    elif self.dealer_isBust() and self.player_isBust() is False:
                        print("Dealer busts")
                        self.player_purse += (2 * self.pot)
                        self.pot = 0
                        break
                    elif self.player_isBust() and self.dealer_isBust() is False:
                        print("Player busts on both hands")
                        self.pot = 0
                        break
                    elif self.dealer_count > self.player_count and self.dealer_count > self.player_secondCount:
                        print("Dealer's hand has higher value than both player's hands")
                        self.pot = 0
                        break
                    elif (self.dealer_count < self.player_count and self.dealer_count > self.player_secondCount) or (self.dealer_count > self.player_count and self.dealer_count < self.player_secondCount):
                        print("One of player's hands beats dealer's hand")
                        self.player_purse += self.pot
                        self.pot = 0
                        break
                    else:
                        print("Both of player's hands beat dealer's hand")
                        self.player_purse += (2 * self.pot)
                        self.pot = 0
                        break

            while True:
                print("\nPlay again? (y/n)")
                player_input = str(input())

                if player_input == "y" or player_input == "Y":
                    # Reset all values to defaults
                    self.game_state = True
                    self.player_hand.clear()
                    self.dealer_hand.clear()
                    self.turn_count = 1
                    self.player_isStand = False
                    self.dealer_isStand = False
                    self.player_count = 0
                    self.player_secondCount = 0
                    self.dealer_count = 0
                    self.instance_deck.clear()
                    self.player_isSplit = False
                    self.player_secondHand.clear()
                    self.player_secondStand = False

                    for i in self.master_deck:
                        self.instance_deck.append(i)

                    shuffle(self.instance_deck)

                    self.player_bet()

                    break
                elif player_input == "n" or player_input == "N":
                    quit()

                print("\nInputted value is not a y or n, try again")



    def player_round(self):
        """
        Dashboard for player to make actions. Prints current hand, status of pot and purse, and dealer's hand (flipped
        card and total cards held). Makes determinations as to what action to show when, prompts user with a menu to
        select next course of action, and ensures that player's input is valid.

        Returns: N/A
        """

        # Print current hand
        print("\nCurrent hand: ")
        self.player_count = 0

        for i in range(0, len(self.player_hand)):
            print(f"{self.player_hand[i][2]} of {self.player_hand[i][0]}")
            self.player_count += self.player_hand[i][1]

        print(f"Current Total: {self.player_count}")

        if self.player_isSplit:
            print("\nSecond hand: ")
            self.player_secondCount = 0

            for i in range(0, len(self.player_secondHand)):
                print(f"{self.player_secondHand[i][2]} of {self.player_secondHand[i][0]}")
                self.player_secondCount += self.player_secondHand[i][1]

            print(f"Current Total: {self.player_secondCount}")

        if self.player_isBust():
            self.game_state = False
            return


        # Print dealer's hand
        print("\nDealer's hand: ")
        for i in range(0, len(self.dealer_hand)):
            if i == 0:
                print(f"{self.dealer_hand[i][2]} of {self.dealer_hand[i][0]}")

        print(f"{len(self.dealer_hand) - 1} face-down card(s)")

        # Print betting information
        print(f"\nPot: {self.pot}")
        print(f"Your Purse: {self.player_purse}")

        if self.player_isSplit is False:
            self.current_action()
        else:
            if self.player_count > 21:
                print("\nFirst hand is bust, skipping")
            else:
                self.current_action()

            if self.player_secondCount > 21:
                #TODO
                print("\nSecond hand is bust, skipping")
            else:
                self.second_action()


    def current_action(self):
        """
        Prints current actions for player. Makes determination as to which actions are available, prompts user for input,
        verifies input, and executes corresponding action.

        Returns: N/A
        """

        # Determine player action
        print("\nWhat is your action?")
        print("[1] Hit")
        print("[2] Stand")

        if self.turn_count == 1 and self.player_hand[0][1] == self.player_hand[1][1]:
            print("[3] Split")

        if self.turn_count == 1:
            print("[4] Double-down")

        while True:
            print("\nEnter corresponding number below: ")
            player_input = int(input())

            if player_input == 1:
                self.player_hit(self.player_hand)
                break
            elif player_input == 2:
                self.player_stand()
                break
            elif player_input == 3 and self.turn_count == 1 and self.player_hand[0][1] == self.player_hand[1][1]:
                self.player_split()
                break
            elif player_input == 4 and self.turn_count == 1:
                self.player_double_down()
                break
            else:
                print("Input was invalid, please try again")

    def second_action(self):
        """
        Prints current actions for player. Makes determination as to which actions are available, prompts user for input,
        verifies input, and executes corresponding action. This is for the second hand when split

        Returns: N/A
        """

        # Determine player action
        print("\nWhat is your action?")
        print("[1] Hit")
        print("[2] Stand")

        while True:
            print("\nEnter corresponding number below: ")
            player_input = int(input())

            if player_input == 1:
                self.player_hit(self.player_secondHand)
                break
            elif player_input == 2:
                self.player_secondStand = True
                break
            else:
                print("Input was invalid, please try again")

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

            if player_bet <= self.player_purse and player_bet > 0:
                self.pot += player_bet
                self.player_purse -= player_bet
                return

            print("\nBet exceeds current purse or is 0, try again")


    def player_hit(self, hand):
        """
        Player hits, which is to draw a card from the deck and add it to their current hand
        in an attempt to get as close to 21 as possible.
        If they player recieves an ace card on their hit,
        they decide if they want it as a 1 or 11 if mathematically possible,
        given the other cards in their hand.

        Args:
            hand: Which hand (list) will the card be appended to

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
        hand.append(new_card)



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
        #TODO

        self.player_isSplit = True

        # Add one card to second hand
        self.player_secondHand.append(self.player_hand.pop())

        # Double bet
        self.pot = self.pot * 2
        self.player_purse -= self.pot / 2


    def player_double_down(self):
        """
        Handling to allow the player to double down during the initial round.
        Doubling down is a chance for the player to
        increase the value of your initial bet by up to 100 per cent.
        You can only double down on your initial turn and it doubles your bet.

        Returns: N/A
        """

        new_purse = self.player_purse - self.pot

        if new_purse < 0:
            print("\nCannot double down, doubling the bet would make purse balance negative")
            self.current_action()

        self.player_purse = new_purse
        self.pot = self.pot * 2


    def player_isBust(self):
        """
        Determines if hand is bust for player.
        A "bust hand" means that you went over 21 points
        and your hand was of no value at all and you lose.

        Returns: Returns true if players hand is busted and false if not.
        """

        if self.player_isSplit is False:
            return self.player_count > 21
        else:
            if self.player_secondCount > 21 and self.player_count > 21:
                return True

    def dealer_round(self):
        """
        Structured instructions for the dealer's hand.
        Manages the CPU's decision making for competing against the player in game.
        The computer/dealer is given the same options as the one playing the game.
        They decide to get more cards or to stay where they are in an attempt to get
        closer to 21 than the player.

        Returns: NaN
        """

        # Checks if first 2 cards received are Aces, and if so, set to 11 value
        for i in range(0, len(self.dealer_hand)):
            if self.dealer_hand[i][1] == 14:
                self.dealer_hand[i][1] = 11

        # Assess dealer count
        for i in range(0, len(self.dealer_hand)):
            self.dealer_count += self.dealer_hand[i][1]

        if self.dealer_isBust():
            self.game_state = False
            return

        # Rules: https://blog.udemy.com/blackjack-rules-2/

        if self.dealer_count < 16:
            self.dealer_hit()

            if self.dealer_hand[len(self.dealer_hand)-1][1] == 14:
                self.dealer_hand[len(self.dealer_hand)-1][1] = 11
            return

            # If total is over 21, check for aces and change value from 11 to 1
        if self.dealer_count > 21:
            for i in range(0, len(self.dealer_hand)):
                if self.dealer_hand[i][1] == 11:
                    self.dealer_hand[i][1] = 1

        if self.dealer_count >= 17:
            self.dealer_stand()
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

        return self.dealer_count > 21


class Blackjack_Test:

    if __name__ == '__main__':
        new_game = Blackjack()

        new_game.game()


