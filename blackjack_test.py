from blackjack import Blackjack

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
