import unittest
from entities.book_tip import BookTip
from entities.tip_types import TipTypes


class TestBookTip(unittest.TestCase):
    def setUp(self):
        self.tip = BookTip()
        self.tip.tip_id = 100
        self.tip.title = "Lord of the Flies"

    def test_tip_type_is_set_correctly(self):
        self.assertEqual(self.tip.tip_type, TipTypes.BOOK)
