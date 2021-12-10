from entities.reading_tip import ReadingTip
from entities.tip_types import TipTypes


class BlogpostTip(ReadingTip):
    """A blogpost typed reading tip class. """

    @property
    def tip_type(self):
        """Returns the tip type."""
        return TipTypes.BLOGPOST

    def set_values_from_dict(self, contents):
        super().set_values_from_dict(contents)
        # Add implementation here

    def get_contents(self):
        contents = super().get_contents()
        # Add implementation here
        return contents
