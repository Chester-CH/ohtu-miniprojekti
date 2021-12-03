class ReadingTip:

    """Class, that describes individual reading tips
    Attributes:
        title: String, which is the name of the reading tips
    """

    def __init__(self, title):
        """Class constructor, which creates a new reading tip.
        Args:
            title: A string, which is the title of the reading tip
        """
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title
