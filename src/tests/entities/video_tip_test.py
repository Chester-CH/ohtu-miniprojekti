import unittest
from entities.video_tip import VideoTip
from entities.tip_types import TipTypes


class TestVideoTip(unittest.TestCase):
    def setUp(self):
        self.tip = VideoTip()
        self.tip.tip_id = 100
        self.tip.title = "Youtube video about Lord of the Flies"

    def test_tip_type_is_set_correctly(self):
        self.assertEqual(self.tip.tip_type, TipTypes.VIDEO)
