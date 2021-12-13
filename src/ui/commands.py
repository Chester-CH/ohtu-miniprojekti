from ui.base_command import Command, QuitSignal
from ui.browse_commands import BrowseTips, RemoveTip, BrowseMenuCommands
from ui.command_factory import CommandFactory, UnknownCommand
from services.reading_tip_factory import ReadingTipFactory
from entities.tip_types import TipTypes


class MainMenuCommands():
    """ Defines all valid main menu command inputs.
    """
    QUIT_PROGRAM = "0"
    ADD_NEW_TIP = "1"
    BROWSE_TIPS = "2"

class SelectTypeMenuCommands():
    TYPE_MENU_COMMANDS = {
        "1": TipTypes.BOOK,
        "2": TipTypes.VIDEO,
        "3": TipTypes.BLOGPOST,
        "4": TipTypes.PODCAST
    }


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
    TIPS_TYPES_TEXT = "\nLukuvinkkien tyypit:\n1: Kirja\n2: Video\n" \
                      "3: Blogpost\n4: Podcast"
    ADD_TYPE_TEXT = "Syötä tyyppi: "
    BAD_TYPE_NUMBER = "Virheellinen syöte"

    def execute(self):
        tips_type = self._select_tips_type()
        input_title = self._io.read(self.ADD_NEW_TIP_TEXT)
        reading_tip = ReadingTipFactory.get_new_reading_tip(tips_type)
        reading_tip["title"] = input_title
        if reading_tip["title"]:
            if self._reading_tip_service.store_reading_tip(reading_tip):
                self._io.write(self.ADDITION_SUCCESS_TEXT)
                return
        self._io.write(self.ADDITION_FAIL_TEXT)

    def _select_tips_type(self):
        self._io.write(self.TIPS_TYPES_TEXT)
        while True:
            type_input = self._io.read(self.ADD_TYPE_TEXT)
            if self._validate_type_input(type_input):
                break
            self._io.write(self.BAD_TYPE_NUMBER)
        return SelectTypeMenuCommands.TYPE_MENU_COMMANDS[type_input]

    def _validate_type_input(self, input):
        try:
            return 0 < int(input) <= 5
        except ValueError:
            return False



def create_main_menu_command_factory(io, reading_tip_service):
    main_menu_commands = {
        MainMenuCommands.QUIT_PROGRAM: QuitProgram(io, reading_tip_service),
        MainMenuCommands.ADD_NEW_TIP: AddNewTip(io, reading_tip_service),
        MainMenuCommands.BROWSE_TIPS: BrowseTips(io, reading_tip_service),
    }
    return CommandFactory(io, reading_tip_service, main_menu_commands)
