from services.reading_tip_service import reading_tip_service as default_reading_tip_service
from console_io import default_console
from ui.commands import QuitSignal, create_main_menu_command_factory


class UI:
    """ The main UI class, holds the start-method. """

    GREET_TEXT = "Hei, tervetuloa Lukuvinkki sovellukseen"
    MENU_TEXT = "\nAnna komento:\n1: lisää lukuvinkki\n2: selaa lukuvinkkejä\n0: lopeta"
    MENU_INPUT_TEXT = "Syötä toiminto: "

    def __init__(self, io=default_console, reading_tip_service=default_reading_tip_service):
        self._io = io
        self._reading_tip_service = reading_tip_service
        self._command_factory = create_main_menu_command_factory(
            io, reading_tip_service)

    def start(self):
        """ Starts running the UI-loop. """
        self._io.write(self.GREET_TEXT)

        try:
            while True:
                self._io.write(self.MENU_TEXT)
                input_string = self._io.read(self.MENU_INPUT_TEXT)
                self._command_factory.get_command(input_string).execute()
        except QuitSignal:
            pass


default_ui = UI()
