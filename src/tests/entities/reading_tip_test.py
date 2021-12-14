import unittest
from unittest.mock import Mock
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

    def test_setting_non_existing_content_type_raises_exception(self):
        with self.assertRaises(KeyError):
            self.tip["something"] = True

    def test_getting_non_existing_content_type_raises_exception(self):
        with self.assertRaises(KeyError):
            value = self.tip["not here"]

    def test_try_set_calls_content_validator(self):
        mock_content = Mock()
        tip = ReadingTip(TipTypes.BOOK, {"big iron": mock_content})
        tip.try_set("big iron", 10)
        mock_content.validator.assert_called_with(10)

    def test_try_set_returns_false_when_validation_fails(self):
        self.assertFalse(self.tip.try_set("title", ""))

    def test_try_set_sets_value_when_validation_passes(self):
        self.tip.try_set("title", "I Robot")
        self.assertEqual(self.tip["title"], "I Robot")
