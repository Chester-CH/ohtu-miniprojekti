from console_io import default_console
from ui.ui import default_ui


class ReadingTipApp:
    """ Tiny base for running the program.
    """

    def __init__(self, ui=default_ui, io=default_console):
        self._io = io
        self._ui = ui

    def run(self):
        """ Runs the program.
        """
        self._ui.start()
