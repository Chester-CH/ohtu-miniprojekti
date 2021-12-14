from entities.content import Content, all_validator


class ReadingTip:
    """ A class for handling singular reading tips.
    """

    def __init__(self, tip_type, contents):
        """ Initializes an empty reading tip. """
        contents["title"] = Content()
        contents["tip_id"] = Content()
        contents["tip_type"] = Content(value=tip_type)
        contents["description"] = Content(validator=all_validator)
        self._contents = contents

    def __setitem__(self, content_type, value):
        if not content_type in self._contents:
            raise KeyError("No such content type.")
        self._contents[content_type].value = value

    def __getitem__(self, content_type):
        if not content_type in self._contents:
            raise KeyError("No such content type.")
        return self._contents[content_type].value

    def set_values_from_dict(self, contents):
        """ Sets corresponding object variables to values indicated
        by the dictionary's key/value pairs.

        Args:
            contents (dict): A dictionary with variable name/value pairs.
        """
        for content_type, value in contents.items():
            if content_type in self._contents:
                self._contents[content_type].value = value

    def get_contents(self):
        """Returns the contents of this tip as a dict. Field names act as keys.
        """
        contents = {}
        for content_type, content in self._contents.items():
            contents[content_type] = content.value
        return contents

    def try_set(self, content_type, value):
        """Tries to set the field (content_type) to value (value). Returns True if 
        validation was successful. """
        content = self._contents[content_type]
        if content.validator(value):
            self[content_type] = value
            return True
        return False
