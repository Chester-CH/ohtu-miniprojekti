# pylint: disable=invalid-name
from mock_io import MockIO
from reading_tip_app import ReadingTipApp
from initialize_database import initialize_database
from database_connection import create_database_connection, TEST_DATABASE_NAME
from repositories.tips_repository import TipsRepository
from ui.ui import UI


class ReadingTipAppLibrary:
    """ The robot library for LukuvinkkiApp.
    """

    def __init__(self):
        self._io = MockIO()
        self._ui = UI(io=self._io)
        self._app = ReadingTipApp(ui=self._ui, io=self._io)

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

    def input_stop_application(self):
        self._io.input_list.append("0")

    def setup_test_database(self):
        """ Wipes the test database clean for each new test.
        """
        self.connection = create_database_connection(TEST_DATABASE_NAME)
        initialize_database(self.connection)
        self.tips_repository = TipsRepository(self.connection)

    def get_greet_message(self):
        return self._ui._greet_text

    def get_menu_message(self):
        return self._ui._menu_text
