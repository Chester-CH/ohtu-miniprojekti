def _default_validator(value):
    """A default validator, return False when value is None or an empty string. """
    if not value:
        return False
    return True

def all_validator(value):
    """No validation for value insertion. Returns True always. """
    # pylint: disable=unused-argument
    return True

class Content:
    """A container class for all content types."""
    def __init__(self, value=None, validator=_default_validator):
        self.validator = validator
        self._value = value

    @property
    def value(self):
        """Returns the content value."""
        return self._value

    @value.setter
    def value(self, new_value):
        if self.validator(new_value):
            self._value = new_value
