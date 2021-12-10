from entities.tip_types import TipTypes


def _get_book_description(book_tip):
    return ""


def _get_blogpost_description(blog_tip):
    return ""


def _get_video_description(video_tip):
    return ""


def _get_podcast_description(podcast_tip):
    return ""


class TipPrinter:
    """ For generating string representations of tip objects in Finnish. """

    TIP_TYPE_PRINTERS = {
        TipTypes.BOOK: _get_book_description,
        TipTypes.BLOGPOST: _get_blogpost_description,
        TipTypes.VIDEO: _get_video_description,
        TipTypes.PODCAST: _get_podcast_description,
    }
    TIP_TYPE_IN_FINNISH = {
        TipTypes.BOOK: "kirja",
        TipTypes.PODCAST: "podcast",
        TipTypes.VIDEO: "video",
        TipTypes.BLOGPOST: "blogiposti"
    }

    @staticmethod
    def get_description(tip):
        """ Returns a string description of the contents of this tip. """
        description = f"{tip.title}, {TipPrinter.TIP_TYPE_IN_FINNISH[tip.tip_type]}" + \
            TipPrinter.TIP_TYPE_PRINTERS[tip.tip_type](tip)
        return description
