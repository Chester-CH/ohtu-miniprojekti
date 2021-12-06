class ReadingTip:

    """Class, that describes individual reading tips
    Attributes:
        title: String, which is the name of the reading tips
    """

    def __init__(self, tip_id, title):
        """Class constructor, which creates a new reading tip.
        Args:
            title: A string, which is the title of the reading tip
        """
        self._title = title
        self._tip_id = tip_id

    @property
    def title(self):
        return self._title

    @property
    def tip_id(self):
        return self._tip_id

    @title.setter
    def title(self, title, tip_id):
        self._title = title
        self._tip_id = tip_id
