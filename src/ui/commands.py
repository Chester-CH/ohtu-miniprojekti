class MainMenuCommands():
    QUIT_PROGRAM = "0"
    ADD_NEW_TIP = "1"
    BROWSE_TIPS = "2"


class Command():
    def __init__(self, io, reading_tip_service):
        self._io = io
        self._reading_tip_service = reading_tip_service


class QuitProgram(Command):
    GOODBYE_TEXT = "Heippa!"

    def execute(self):
        self._io.write(self.GOODBYE_TEXT)
        raise Exception("Quit-signal")


class AddNewTip(Command):
    ADDITION_SUCCESS_TEXT = "Uuden lukuvinkin luonti onnistui."
    ADDITION_FAIL_TEXT = "Uuden lukuvinkin luonti epäonnistui."
    ADD_NEW_TIP_TEXT = "Kirjoita otsikko: "

    def execute(self):
        input_title = self._io.read(self.ADD_NEW_TIP_TEXT)
        reading_tip = self._reading_tip_service.create_reading_tip(input_title)
        if reading_tip is not None:
            self._io.write(self.ADDITION_SUCCESS_TEXT)
        else:
            self._io.write(self.ADDITION_FAIL_TEXT)


class BrowseTips(Command):
    GREET_TEXT = "Selaa lukuvinkkejä:"
    COMMAND_HELP_TEXT = "Komennot: 0: lopeta, 1: Seuraava sivu"
    TIPS_PER_PAGE = 10

    class MenuCommands:
        STOP = "0"
        NEXT_PAGE = "1"

    def execute(self):
        self._io.write(self.GREET_TEXT)
        # NOT IMPLEMENTED


class UnknownCommand(Command):
    UNKNOWN_COMMAND_TEXT = "Tuntematon syöte."

    def execute(self):
        self._io.write(self.UNKNOWN_COMMAND_TEXT)


class CommandFactory():
    def __init__(self, io, reading_tip_service, commands=None):
        self._io = io
        self._reading_tip_service = reading_tip_service
        if not commands:
            commands = {
                MainMenuCommands.QUIT_PROGRAM: QuitProgram(self._io, self._reading_tip_service),
                MainMenuCommands.ADD_NEW_TIP: AddNewTip(self._io, self._reading_tip_service),
                MainMenuCommands.BROWSE_TIPS: BrowseTips(self._io, self._reading_tip_service),
            }
        self._commands = commands

    def get_command(self, command_string):
        return self._commands.get(command_string,
                                  UnknownCommand(self._io, self._reading_tip_service))
