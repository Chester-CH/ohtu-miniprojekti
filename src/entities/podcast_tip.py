from entities.reading_tip import ReadingTip
from entities.tip_types import TipTypes


class PodcastTip(ReadingTip):
    """A podcast typed reading tip class. """

    @property
    def tip_type(self):
        """Returns the tip type."""
        return TipTypes.PODCAST

    def set_values_from_dict(self, contents):
        super().set_values_from_dict(contents)
        # Add implementation here

    def get_contents(self):
        contents = super().get_contents()
        # Add implementation here
        return contents
