import unittest
from poker.card import Card


class CardTest(unittest.TestCase):
    def test_has_rank(self):
        card = Card(rank="Queen", suit="Hearts")
        self.assertEqual(card.rank, "Queen")

    def test_has_suit(self):
        card = Card(rank="2", suit="Clubs")
        self.assertEqual(card.suit, "Clubs")

    def test_knows_its_rank_index(self):
        card = Card(rank="Queen", suit="Hearts")
        self.assertEqual(card.rank_index, 10)

    def test_has_string_representation(self):
        card = Card(rank="5", suit="Diamonds")
        self.assertEqual(str(card), "5 of Diamonds")

    def test_has_tech_representation(self):
        card = Card(rank="5", suit="Diamonds")
        self.assertEqual(repr(card), "Card('5', 'Diamonds')")

    def test_card_has_4_suit_options(self):
        self.assertEqual(
            Card.SUITS,
            ("Hearts", "Clubs", "Spades", "Diamonds")
        )

    def test_card_has_13_rank_options(self):
        self.assertEqual(
            Card.RANKS,
            ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace")
        )

    def test_card_only_allows_valid_rank(self):
        with self.assertRaises(ValueError):
            Card(rank="Two", suit="Diamonds")

    def test_card_only_allows_valid_suit(self):
        with self.assertRaises(ValueError):
            Card(rank="2", suit="Diamond")

    def test_can_create_standard_52_card(self):
        cards = Card.create_standard_52_card()
        self.assertEqual(len(cards), 52)

        self.assertEqual(cards[0], Card(rank="2", suit="Hearts"))
        self.assertEqual(cards[-1], Card(rank="Ace", suit="Diamonds"))

    def test_card_can_sort_itself_with_another_card(self):
        queen_of_spades = Card(rank="Queen", suit="Spades")
        king_of_spades = Card(rank="King", suit="Spades")
        result = queen_of_spades < king_of_spades
        self.assertEqual(result, True)

    def test_sort_cards(self):
        two_of_spades = Card(rank="2", suit="Spades")
        five_of_diamonds = Card(rank="5", suit="Diamonds")
        five_of_hearts = Card(rank="5", suit="Hearts")
        eight_of_hearts = Card(rank="8", suit="Hearts")
        ace_of_clubs = Card(rank="Ace", suit="Clubs")

        unsorted_cards = [
            five_of_diamonds,
            two_of_spades,
            five_of_hearts,
            ace_of_clubs,
            eight_of_hearts
        ]

        # 同じランクであれば、先に入っている five_of_diamonds が上位に来る。
        unsorted_cards.sort()

        self.assertEqual(
            unsorted_cards,
            [
                two_of_spades,
                five_of_diamonds,
                five_of_hearts,
                eight_of_hearts,
                ace_of_clubs
            ]
        )
