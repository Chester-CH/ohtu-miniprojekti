import unittest
from unittest.mock import Mock
from services.reading_tip_service import ReadingTipService
from services.reading_tip_factory import ReadingTipFactory
from entities.tip_types import TipTypes


def mock_remove_fails(tip_id):
    return False


class TestReadingTipService(unittest.TestCase):
    def setUp(self):
        self.repository = Mock()
        self.service = ReadingTipService(self.repository)

    def test_remove_reading_tip_calls_repository_with_tip(self):
        tip = ReadingTipFactory.get_new_reading_tip(TipTypes.BLOGPOST)
        tip["tip_id"] = 10
        self.service.remove_reading_tip(tip)
        self.repository.remove_tip.assert_called_with(10)

    def test_remove_reading_tip_does_not_call_repository_on_None(self):
        self.service.remove_reading_tip(None)
        self.repository.remove_tip.assert_not_called()

    def test_remove_reading_tip_does_not_call_repository_on_tips_with_no_id(self):
        tip = ReadingTipFactory.get_new_reading_tip(TipTypes.BLOGPOST)
        self.service.remove_reading_tip(tip)
        self.repository.remove_tip.assert_not_called()

    def test_remove_reading_tip_returns_false_if_repository_fails(self):
        tip = ReadingTipFactory.get_new_reading_tip(TipTypes.BLOGPOST)
        tip["tip_id"] = 10
        self.repository.remove_tip = lambda tip_id: False
        self.assertFalse(self.service.remove_reading_tip(tip))

    def test_store_reading_tip_does_not_call_repository_on_None(self):
        self.service.store_reading_tip(None)
        self.repository.store_reading_tip.assert_not_called()

    def test_store_reading_tip_calls_repository_on_valid_tip(self):
        tip = ReadingTipFactory.get_new_reading_tip(TipTypes.BLOGPOST)
        self.service.store_reading_tip(tip)
        self.repository.store_reading_tip.assert_called_with(tip)

    def test_store_reading_tip_returns_false_if_repository_fails(self):
        tip = ReadingTipFactory.get_new_reading_tip(TipTypes.BLOGPOST)
        self.repository.store_reading_tip = lambda tip: False
        self.assertFalse(self.service.store_reading_tip(tip))
