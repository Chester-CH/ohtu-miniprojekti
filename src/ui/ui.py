from services.reading_tip_service import reading_tip_service as default_reading_tip_service
from console_io import default_console
from ui.commands import CommandFactory, QuitSignal


class UI:
    GREET_TEXT = "Hei, tervetuloa Lukuvinkki sovellukseen"
    MENU_TEXT = "\nAnna komento:\n1: lisää lukuvinkki\n2: selaa lukuvinkkejä\n0: lopeta"
    MENU_INPUT_TEXT = "Syötä toiminto: "

    def __init__(self, io=default_console, reading_tip_service=default_reading_tip_service):
        self._io = io
        self._reading_tip_service = reading_tip_service
        self._command_factory = CommandFactory(io, reading_tip_service)

    def start(self):
        self._io.write(self.GREET_TEXT)

        try:
            while True:
                self._io.write(self.MENU_TEXT)
                input_string = self._io.read(self.MENU_INPUT_TEXT)
                self._command_factory.get_command(input_string).execute()
        except QuitSignal:
            pass


default_ui = UI()
