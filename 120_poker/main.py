from poker.card import Card
from poker.deck import Deck
from poker.hand import Hand
from poker.player import Player

deck = Deck()
cards = Card.create_standard_52_card()
deck.add_cards(cards)

hand1 = Hand(cards=[])
player1 = Player(name="Boris", hand=hand1)

hand2 = Hand(cards=[])
player2 = Player(name="Bobby", hand=hand2)
