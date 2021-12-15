# pylint: disable=unused-import
# These are also used from the robot files.
from ui.base_command import Command, QuitSignal
from ui.browse_commands import BrowseTips, RemoveTip, BrowseMenuCommands
from ui.add_new_tip_command import AddNewTip
from ui.command_factory import CommandFactory, UnknownCommand
from services.reading_tip_factory import ReadingTipFactory
from entities.tip_types import TipTypes


class MainMenuCommands():
    """ Defines all valid main menu command inputs.
    """
    QUIT_PROGRAM = "0"
    ADD_NEW_TIP = "1"
    BROWSE_TIPS = "2"


class QuitProgram(Command):
    """ A small command for quitting the program from the main menu.
    """
    GOODBYE_TEXT = "Heippa!"

    def execute(self):
        """ Prints out the quit message to the console.

        Raises:
            Exception: used to signal to the main loop that the user wishes to quit.
        """
        self._io.write(self.GOODBYE_TEXT)
        raise QuitSignal


def create_main_menu_command_factory(io, reading_tip_service):
    """ Creates a new main menu command factory used by the main ui-loop. """
    # Nothing wrong with 'io'.
    # pylint: disable=invalid-name
    main_menu_commands = {
        MainMenuCommands.QUIT_PROGRAM: QuitProgram(io, reading_tip_service),
        MainMenuCommands.ADD_NEW_TIP: AddNewTip(io, reading_tip_service),
        MainMenuCommands.BROWSE_TIPS: BrowseTips(io, reading_tip_service),
    }
    return CommandFactory(io, reading_tip_service, main_menu_commands)
