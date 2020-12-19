from blackjack import Blackjack
from blackjack import Deck


def test_player_stand():
    """Does player stand function when the isStand variable is set"""
    blackjack_test = Blackjack()
    blackjack_test.player_stand()
    assert blackjack_test.player_isStand == True


def test_player_stand_split():
    """Does player stand function when the isStand variable is set for the split condition, where both the first
    and second hand are currently standing"""
    blackjack_test = Blackjack()
    blackjack_test.player_isSplit = True
    blackjack_test.player_firstStand = True
    blackjack_test.player_secondStand = True
    blackjack_test.player_stand()
    assert blackjack_test.player_isStand == True


def test_dealer_stand():
    """Does dealer stand function when dealer_stand function is ran"""
    blackjack_test = Blackjack()
    blackjack_test.dealer_stand()
    assert blackjack_test.dealer_isStand == True


def test_deck_init():
    """Tests the __init__() function within the Deck class to ensure that the deck of card objects is made properly
    """
    test_deck = Deck()
    test_cards = Deck.get_cards(test_deck)

    assert ("Clubs", 10, "Jack") in test_cards
    assert ("Spades", 10, "Queen") in test_cards
    assert ("Hearts", 10, "King") in test_cards
    assert ("Diamonds", 10, "Ace") in test_cards

def test_get_cards():
    """
    Tests the get_cards() method under Deck to ensure that the datatype returned is a list of tuples
    """

    test_deck = Deck()

    assert type(test_deck.get_cards()) is list
