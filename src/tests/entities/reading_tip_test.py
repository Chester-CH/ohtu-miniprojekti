import unittest
from entities.reading_tip import ReadingTip


class TestReadingTip(unittest.TestCase):
    def setUp(self):
        self.tip = ReadingTip()
        self.tip.tip_id = 100
        self.tip.title = "Lord of the Flies"

    def test_set_values_from_dict_sets_the_correct_values(self):
        values = {"tip_id": 1, "title": "Lord of the Rings"}
        self.tip.set_values_from_dict(values)
        self.assertEqual(self.tip.tip_id, 1)
        self.assertEqual(self.tip.title, "Lord of the Rings")

    def test_get_contents_returns_correct_values(self):
        values = self.tip.get_contents()
        self.assertEqual(values["tip_id"], 100)
        self.assertEqual(values["title"], "Lord of the Flies")

    def test_get_contents_does_not_return_none_values(self):
        tip = ReadingTip()
        values = tip.get_contents()
        self.assertFalse("tip_id" in values)
