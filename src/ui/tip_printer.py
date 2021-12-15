from entities.tip_types import TipTypes


def _get_field_description(user_text, content_type, tip):
    if tip[content_type]:
        return user_text + str(tip[content_type])
    return False


def _get_book_description(book_tip):
    descriptions = [_get_field_description("Kirjailija: ", "author", book_tip),
                    _get_field_description("ISBN: ", "isbn", book_tip),
                    _get_field_description("Kuvaus: ", "description", book_tip)]
    return "\n".join(filter(lambda s: s, descriptions))


def _get_blogpost_description(blog_tip):
    descriptions = [_get_field_description("Tekijä: ", "author", blog_tip),
                    _get_field_description("URL: ", "url", blog_tip),
                    _get_field_description("Kuvaus: ", "description", blog_tip)]
    return "\n".join(filter(lambda s: s, descriptions))


def _get_video_description(video_tip):
    descriptions = [_get_field_description("URL: ", "url", video_tip),
                    _get_field_description("Kuvaus: ", "description", video_tip)]
    return "\n".join(filter(lambda s: s, descriptions))


def _get_podcast_description(podcast_tip):
    descriptions = [_get_field_description("Nimi: ", "name", podcast_tip),
                    _get_field_description("Tekijä: ", "author", podcast_tip),
                    _get_field_description("URL: ", "url", podcast_tip),
                    _get_field_description("Kuvaus: ", "description", podcast_tip)]
    return "\n".join(filter(lambda s: s, descriptions))


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
        str_representation = TipPrinter.TIP_TYPE_PRINTERS[tip['tip_type']](tip)
        str_representation = f"{tip['title']}," + \
            f" {TipPrinter.TIP_TYPE_IN_FINNISH[tip['tip_type']]}" + \
            "\n" + str_representation + "\n"
        return str_representation
