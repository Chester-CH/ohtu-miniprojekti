import unittest
from entities.podcast_tip import PodcastTip
from entities.tip_types import TipTypes


class TestPodcastTip(unittest.TestCase):
    def setUp(self):
        self.tip = PodcastTip()
        self.tip.tip_id = 100
        self.tip.title = "Podcast about Lord of the Flies"

    def test_tip_type_is_set_correctly(self):
        self.assertEqual(self.tip.tip_type, TipTypes.PODCAST)
