import unittest
from entities.reading_tip import ReadingTip
from entities.tip_types import TipTypes
from entities.content import Content


class TestReadingTip(unittest.TestCase):
    def setUp(self):
        self.tip = ReadingTip(TipTypes.BOOK, {})
        self.tip["tip_id"] = 100
        self.tip["title"] = "Lord of the Flies"

    def test_set_values_from_dict_sets_the_correct_values(self):
        values = {"tip_id": 1, "title": "Lord of the Rings"}
        self.tip.set_values_from_dict(values)
        self.assertEqual(self.tip["tip_id"], 1)
        self.assertEqual(self.tip["title"], "Lord of the Rings")

    def test_get_contents_returns_correct_values(self):
        values = self.tip.get_contents()
        self.assertEqual(values["tip_id"], 100)
        self.assertEqual(values["title"], "Lord of the Flies")

    def test_set_values_from_dict_sets_only_content_types_in_tip(self):
        tip = ReadingTip(TipTypes.BOOK, {"author": Content()})
        new_contents = {"author": "Asimov", "url": "www.google.com"}
        tip.set_values_from_dict(new_contents)
        contents = tip.get_contents()
        self.assertEqual(contents["author"], "Asimov")
        self.assertTrue("url" not in contents)
