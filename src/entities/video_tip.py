from entities.reading_tip import ReadingTip
from entities.tip_types import TipTypes


class VideoTip(ReadingTip):
    """A video typed reading tip class. """
    TYPE = TipTypes.VIDEO
