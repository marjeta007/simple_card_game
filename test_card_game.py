import unittest

from card import Card


class CardGameTestCase(unittest.TestCase):

    def test_new_random_card(self):
        card = Card()
        self.assertTrue(card.number in card.number_list)
        self.assertTrue(card.color in card.color_list)

    def test_new_card(self):
        for color in Card.color_list:
            for number in Card.number_list:
                card = Card(color, number)
                self.assertEqual(card.color, color)
                self.assertEqual(card.number, number)

    def test_new_card2(self):
        for color in Card.color_list:
            for number in Card.number_list:
                card = Card(number=number, color=color)
                self.assertEqual(card.color, color)
                self.assertEqual(card.number, number)

    def test_bad_color(self):
        self.assertRaises(ValueError,
                          Card,
                          number=8,
                          color='aquamarine')

    def test_bad_number(self):
        self.assertRaises(ValueError,
                          Card,
                          number=42,
                          color='yellow')

    def test_bad_number_and_color(self):
        self.assertRaises(ValueError,
                          Card,
                          number=42,
                          color='turquoise')

    def test_something_TT(self):
        self.assertEqual(True, True)

    def test_something_FF(self):
        self.assertEqual(False, False)


if __name__ == '__main__':
    unittest.main()
