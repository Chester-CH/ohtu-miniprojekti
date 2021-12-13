from entities.tip_types import TipTypes
from entities.reading_tip import ReadingTip
from entities.content import Content


def _create_new_book_tip():
    contents = {"author": Content(), "isbn": Content()}
    tip = ReadingTip(TipTypes.BOOK, contents)
    return tip


def _create_new_video_tip():
    contents = {"url": Content()}
    tip = ReadingTip(TipTypes.VIDEO, contents)
    return tip


def _create_new_blogpost_tip():
    contents = {"url": Content(), "author": Content()}
    tip = ReadingTip(TipTypes.BLOGPOST, contents)
    return tip


def _create_new_podcast_tip():
    contents = {"url": Content(), "author": Content(),
                "name": Content()}
    tip = ReadingTip(TipTypes.PODCAST, contents)
    return tip


class ReadingTipFactory:
    """A factory class for creating new reading tips of various types.
    """
    _TIP_CONSTRUCTORS = {
        TipTypes.BOOK: _create_new_book_tip,
        TipTypes.VIDEO: _create_new_video_tip,
        TipTypes.BLOGPOST: _create_new_blogpost_tip,
        TipTypes.PODCAST: _create_new_podcast_tip}

    @staticmethod
    def get_new_reading_tip(tip_type):
        """Returns a new empty reading tip. Entirely transient, until stored
        through reading tip service.

        Args:
            type (str): The type of the reading tip ('book', 'video', 'podcast' or
            'blogpost'.) See entities.tip_types.

        Returns:
            ReadingTip: Returns a new empty reading tip object.
        """
        if tip_type in ReadingTipFactory._TIP_CONSTRUCTORS:
            return ReadingTipFactory._TIP_CONSTRUCTORS[tip_type]()
        raise ValueError("Wrong type")
