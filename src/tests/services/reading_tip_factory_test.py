import unittest
from services.reading_tip_factory import ReadingTipFactory
from entities.tip_types import TipTypes


class TestReadingTipFactory(unittest.TestCase):
    def test_get_new_reading_tip_returns_book_type_correctly(self):
        tip = ReadingTipFactory.get_new_reading_tip(TipTypes.BOOK)
        self.assertEqual(tip["tip_type"], TipTypes.BOOK)

    def test_get_new_reading_tip_returns_podcast_type_correctly(self):
        tip = ReadingTipFactory.get_new_reading_tip(TipTypes.PODCAST)
        self.assertEqual(tip["tip_type"], TipTypes.PODCAST)

    def test_get_new_reading_tip_returns_video_type_correctly(self):
        tip = ReadingTipFactory.get_new_reading_tip(TipTypes.VIDEO)
        self.assertEqual(tip["tip_type"], TipTypes.VIDEO)

    def test_get_new_reading_tip_returns_blogpost_type_correctly(self):
        tip = ReadingTipFactory.get_new_reading_tip(TipTypes.BLOGPOST)
        self.assertEqual(tip["tip_type"], TipTypes.BLOGPOST)
