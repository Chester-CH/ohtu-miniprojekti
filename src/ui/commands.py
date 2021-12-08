from ui.base_command import Command, QuitSignal
from ui.browse_commands import BrowseTips, RemoveTip, BrowseMenuCommands
from ui.command_factory import CommandFactory, UnknownCommand


class MainMenuCommands():
    """ Defines all valid main menu command inputs.
    """
    QUIT_PROGRAM = "0"
    ADD_NEW_TIP = "1"
    BROWSE_TIPS = "2"


class QuitProgram(Command):
    """ Command for quitting the program.
    """
    GOODBYE_TEXT = "Heippa!"

    def execute(self):
        """ Prints out the quit message to the console.

        Raises:
            Exception: used to signal to the main loop that the user wishes to quit.
        """
        self._io.write(self.GOODBYE_TEXT)
        raise QuitSignal


class AddNewTip(Command):
    """ Command for adding a new tip, should contain all menu handling for it.
    """
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


def create_main_menu_command_factory(io, reading_tip_service):
    main_menu_commands = {
        MainMenuCommands.QUIT_PROGRAM: QuitProgram(io, reading_tip_service),
        MainMenuCommands.ADD_NEW_TIP: AddNewTip(io, reading_tip_service),
        MainMenuCommands.BROWSE_TIPS: BrowseTips(io, reading_tip_service),
    }
    return CommandFactory(io, reading_tip_service, main_menu_commands)
