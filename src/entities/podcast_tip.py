from entities.reading_tip import ReadingTip
from entities.tip_types import TipTypes


class PodcastTip(ReadingTip):
    """A podcast typed reading tip class. """
    TYPE = TipTypes.PODCAST
