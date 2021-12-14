# pylint: skip-file
from mock_io import MockIO
from reading_tip_app import ReadingTipApp
from initialize_database import initialize_database
from database_connection import create_database_connection, TEST_DATABASE_NAME
from repositories.tips_repository import TipsRepository
from services.reading_tip_service import ReadingTipService
from ui.ui import UI
import ui.commands as commands


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
        for output_message in self._io.output_list:
            if message in output_message:
                return

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

    def get_ui_message(self, command_type, message_type):
        if command_type == "MainMenu":
            return getattr(self._ui, message_type)
        else:
            return getattr(getattr(commands, command_type), message_type)

    def program_remembers_tip(self, tip_title):
        sql = "SELECT title FROM Tips WHERE title=?;"
        cursor = self.connection.cursor()
        answer = cursor.execute(sql, [tip_title]).fetchone()
        if answer[0] != tip_title:
            raise AssertionError(
                f"The tip with title {tip_title} was not saved.")

    def program_doesnt_show_tip(self, tip_title):
        sql = "SELECT visible FROM Tips WHERE title=?;"
        cursor = self.connection.cursor()
        answer = cursor.execute(sql, [tip_title]).fetchone()
        if answer[0]:
            raise AssertionError(
                f"The tip titled {tip_title} is visible."
            )
    
    def check_tips_title_and_type_match(self, title, type):
        sql = "SELECT title, type FROM Tips WHERE title=:title;"
        cursor = self.connection.cursor()
        answers = cursor.execute(sql, {"title":title, "type":type}).fetchall()[0]
        if title != answers[0] and type != answers[1]:
            raise AssertionError(
                f"Tips title {title} doesn't mach {type}\
                  which are {answers[0]} and {answers[1]}"
            )
