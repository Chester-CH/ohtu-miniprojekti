from entities.book_tip import BookTip
from entities.video_tip import VideoTip
from entities.blogpost_tip import BlogpostTip
from entities.podcast_tip import PodcastTip


class ReadingTipFactory:
    """A factory class for creating new reading tips of various types.
    """
    _TIP_CLASSES = {
        BookTip.TYPE: BookTip,
        VideoTip.TYPE: VideoTip,
        BlogpostTip.TYPE: BlogpostTip,
        PodcastTip.TYPE: PodcastTip
    }

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
        if tip_type in ReadingTipFactory._TIP_CLASSES:
            return ReadingTipFactory._TIP_CLASSES[tip_type]()
        raise ValueError("Wrong type")
