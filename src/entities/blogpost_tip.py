from entities.reading_tip import ReadingTip
from entities.tip_types import TipTypes


class BlogpostTip(ReadingTip):
    """A blogpost typed reading tip class. """
    TYPE = TipTypes.BLOGPOST
