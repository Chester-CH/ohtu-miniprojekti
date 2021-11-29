from console_io import ConsoleIO


class ReadingTipApp:
    """ Tiny base for running the program.
    """

    def __init__(self, io=None):
        if not io:
            io = ConsoleIO()
        self._io = io

    def run(self):
        """ Runs the program.
        """
        self._io.write("Hello world!")
