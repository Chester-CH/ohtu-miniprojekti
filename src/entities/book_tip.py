from entities.reading_tip import ReadingTip
from entities.tip_types import TipTypes


class BookTip(ReadingTip):
    """A book typed reading tip class. """
    TYPE = TipTypes.BOOK
