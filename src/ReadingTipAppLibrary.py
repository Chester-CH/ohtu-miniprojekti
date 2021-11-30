# pylint: skip-file
from mock_io import MockIO
from reading_tip_app import ReadingTipApp
from initialize_database import initialize_database
from database_connection import create_database_connection, TEST_DATABASE_NAME
from repositories.tips_repository import TipsRepository
from services.reading_tip_service import ReadingTipService
from ui.ui import UI


class ReadingTipAppLibrary:
    """ The robot library for LukuvinkkiApp.
    """

    def __init__(self):
        self.connection = create_database_connection(TEST_DATABASE_NAME)
        initialize_database(self.connection)
        self.tips_repository = TipsRepository(self.connection)
        self.reading_tip_service = ReadingTipService(self.tips_repository)
        self._io = MockIO()
        self._ui = UI(
            io=self._io, reading_tip_service=self.reading_tip_service)
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
        self.input_command("0")

    def input_command(self, command):
        self._io.input_list.append(command)

    def get_ui_message(self, message_type):
        return getattr(self._ui, message_type)

    def program_remembers_tip(self, tip_title):
        sql = "SELECT title FROM Tips;"
        cursor = self.connection.cursor()
        answer = cursor.execute(sql).fetchone()
        if answer[0] != tip_title:
            raise AssertionError(
                f"The tip with title {tip_title} was not saved.")
