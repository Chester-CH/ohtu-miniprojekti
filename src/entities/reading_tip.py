from entities.tip_types import TipTypes


class ReadingTip:
    """Class, that describes base reading tips
    """

    def __init__(self):
        """ Initializes an empty base reading tip. """
        self._contents = {"type": self.tip_type}

    @property
    def tip_id(self):
        """Returns the tip id, or None.
        """
        return self._contents.get("tip_id", None)

    @tip_id.setter
    def tip_id(self, tip_id):
        """Sets the tip id."""
        if tip_id:
            self._contents["tip_id"] = tip_id

    @property
    def title(self):
        """Returns the tip title, or None."""
        return self._contents.get("title", None)

    @title.setter
    def title(self, title):
        """Sets the title."""
        if title:
            self._contents["title"] = title

    @property
    def tip_type(self):
        """Returns the tip type."""
        return TipTypes.UNDEFINED

    def set_values_from_dict(self, contents):
        """ Sets corresponding object variables to values indicated
        by the dictionary's key/value pairs.

        Args:
            contents (dict): A dictionary with variable name/value pairs.
        """
        self.tip_id = contents["tip_id"]
        self.title = contents["title"]

    def get_contents(self):
        """Returns the contents of this tip as a dict. Field names act as keys.
        The dict only contains not-None values.
        """
        contents = {}
        for key, value in self._contents.items():
            if value:
                contents[key] = value
        return contents
