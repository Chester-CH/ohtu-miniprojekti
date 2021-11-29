# pylint: disable=invalid-name
from mock_io import MockIO
from reading_tip_app import ReadingTipApp


class ReadingTipAppLibrary:
    """ The robot library for LukuvinkkiApp.
    """

    def __init__(self):
        self._io = MockIO()
        self._app = ReadingTipApp(self._io)

    def output_should_contain(self, message):
        """ Raises an AssertionError when the output didn't contain message.
        """
        if not message in self._io.output_list:
            raise AssertionError(
                f"Missing output \"{message}\" in {str(self._io.output_list)}")

    def run_application(self):
        """ Runs the application for robot tests.
        """
        self._app.run()
