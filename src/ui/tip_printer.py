from entities.tip_types import TipTypes


def _value_string(value):
    if value:
        return str(value)
    return ""


def _add_description(string_description, tip):
    if tip['description']:
        string_description += f"\nKuvaus: {_value_string(tip['description'])}"
    return string_description


def _get_book_description(book_tip):
    string_description = "\n" + \
        f"Kirjailija: {_value_string(book_tip['author'])}, " + \
        f"ISBN: {_value_string(book_tip['isbn'])}"
    return _add_description(string_description, book_tip)


def _get_blogpost_description(blog_tip):
    string_description = "\n" + \
        f"Tekijä: {_value_string(blog_tip['author'])}, " + \
        f"URL: {_value_string(blog_tip['url'])}"
    return _add_description(string_description, blog_tip)


def _get_video_description(video_tip):
    string_description = "\n" + \
        f"URL: {_value_string(video_tip['url'])}"
    return _add_description(string_description, video_tip)


def _get_podcast_description(podcast_tip):
    string_description = "\n" + \
        f"Podcastin nimi: {_value_string(podcast_tip['name'])}, " + \
        f"Tekijä: {_value_string(podcast_tip['author'])}\n" + \
        f"URL: {_value_string(podcast_tip['url'])}"
    return _add_description(string_description, podcast_tip)


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
        description = f"{tip['title']}, {TipPrinter.TIP_TYPE_IN_FINNISH[tip['tip_type']]}" + \
            TipPrinter.TIP_TYPE_PRINTERS[tip['tip_type']](tip) + "\n"
        return description
