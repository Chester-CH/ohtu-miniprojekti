import unittest
from services.reading_tip_factory import ReadingTipFactory
from entities.tip_types import TipTypes


class TestReadingTipFactory(unittest.TestCase):
    def test_get_new_reading_tip_returns_book_type_correctly(self):
        tip = ReadingTipFactory.get_new_reading_tip(TipTypes.BOOK)
        self.assertEqual(tip["tip_type"], TipTypes.BOOK)

    def test_new_book_tips_have_the_correct_content_fields(self):
        tip = ReadingTipFactory.get_new_reading_tip(TipTypes.BOOK)
        contents = tip.get_contents()
        self.assertTrue("tip_id" in contents)
        self.assertTrue("title" in contents)
        self.assertTrue("description" in contents)
        self.assertTrue("author" in contents)
        self.assertTrue("isbn" in contents)
        self.assertFalse("url" in contents)

    def test_get_new_reading_tip_returns_podcast_type_correctly(self):
        tip = ReadingTipFactory.get_new_reading_tip(TipTypes.PODCAST)
        self.assertEqual(tip["tip_type"], TipTypes.PODCAST)

    def test_new_podcast_tips_have_the_correct_fields(self):
        tip = ReadingTipFactory.get_new_reading_tip(TipTypes.PODCAST)
        contents = tip.get_contents()
        self.assertTrue("tip_id" in contents)
        self.assertTrue("title" in contents)
        self.assertTrue("description" in contents)
        self.assertTrue("author" in contents)
        self.assertTrue("name" in contents)
        self.assertFalse("isbn" in contents)
        self.assertTrue("url" in contents)

    def test_get_new_reading_tip_returns_video_type_correctly(self):
        tip = ReadingTipFactory.get_new_reading_tip(TipTypes.VIDEO)
        self.assertEqual(tip["tip_type"], TipTypes.VIDEO)

    def test_new_video_tips_have_the_correct_fields(self):
        tip = ReadingTipFactory.get_new_reading_tip(TipTypes.VIDEO)
        contents = tip.get_contents()
        self.assertTrue("tip_id" in contents)
        self.assertTrue("title" in contents)
        self.assertTrue("description" in contents)
        self.assertFalse("author" in contents)
        self.assertFalse("isbn" in contents)
        self.assertTrue("url" in contents)

    def test_get_new_reading_tip_returns_blogpost_type_correctly(self):
        tip = ReadingTipFactory.get_new_reading_tip(TipTypes.BLOGPOST)
        self.assertEqual(tip["tip_type"], TipTypes.BLOGPOST)

    def test_new_blogpost_tips_have_the_correct_fields(self):
        tip = ReadingTipFactory.get_new_reading_tip(TipTypes.BLOGPOST)
        contents = tip.get_contents()
        self.assertTrue("tip_id" in contents)
        self.assertTrue("title" in contents)
        self.assertTrue("description" in contents)
        self.assertTrue("author" in contents)
        self.assertFalse("isbn" in contents)
        self.assertTrue("url" in contents)
