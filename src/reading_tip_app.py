from console_io import ConsoleIO
from ui.ui import default_ui


class ReadingTipApp:
    """ Tiny base for running the program.
    """

    def __init__(self, ui=default_ui, io=None):
        if not io:
            io = ConsoleIO()
        self._io = io
        self._ui = ui

    def run(self):
        """ Runs the program.
        """
        self._ui.start()
