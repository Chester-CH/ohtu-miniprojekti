class QuitSignal(Exception):
    """ Used to get out of command loops with a quit command. """
    # pylint: disable=unnecessary-pass
    pass

class Command():
    """ A generic base class for handling user inputs.
    """

    def __init__(self, io, reading_tip_service):
        self._io = io
        self._reading_tip_service = reading_tip_service
