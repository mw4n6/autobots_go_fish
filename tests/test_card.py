import unittest
from unittest import TestCase
from classes.card import Card
from constants.card import SUITS, RANKS

class CardTest():
	def test_number(self):
		card = Card(SUITS[0], RANKS[0]);
		self.assertEqual(card.suit, 'Clubs', msg="Card's suit is not clubs");

	def test_suit(self):
		card = Card(SUITS[0], RANKS[0]);
		self.assertEqual(card.rank, 'A', msg="Card's rank is not Ace");

if __name__ == '__main__':
    unittest.main();
