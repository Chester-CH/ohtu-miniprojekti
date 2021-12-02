from services.reading_tip_service import ReadingTipService
import unittest
from unittest.mock import Mock

class TestReadingTipService(unittest.TestCase):
    def setUp(self):
        self.repository = Mock()
        self.service = ReadingTipService(self.repository)
    
    def test_create_rreading_tip_gives_reposytory_right_title(self):
        title = "Some_Title"
        self.service.create_reading_tip(title)
        self.repository.create_tip.assert_called_with(title)
