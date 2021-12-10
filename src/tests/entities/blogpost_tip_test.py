import unittest
from entities.blogpost_tip import BlogpostTip
from entities.tip_types import TipTypes


class TestBlogpostTip(unittest.TestCase):
    def setUp(self):
        self.tip = BlogpostTip()
        self.tip.tip_id = 100
        self.tip.title = "Blogpost about Lord of the Flies"

    def test_tip_type_is_set_correctly(self):
        self.assertEqual(self.tip.tip_type, TipTypes.BLOGPOST)
