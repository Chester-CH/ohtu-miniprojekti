class MainMenuCommands():
    """ Defines all valid main menu command inputs.
    """
    QUIT_PROGRAM = "0"
    ADD_NEW_TIP = "1"
    BROWSE_TIPS = "2"


class Command():
    """ A generic base class for handling user inputs.
    """

    def __init__(self, io, reading_tip_service):
        self._io = io
        self._reading_tip_service = reading_tip_service


class QuitSignal(Exception):
    pass


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


class BrowseTips(Command):
    """ Command for browsing the created tips list.
    """
    GREET_TEXT = "\nSelaa lukuvinkkejä:"
    COMMAND_HELP_TEXT = "Komennot: 0: lopeta, 1: Seuraava sivu"
    QUERY_FOR_MORE_TEXT = "Tulosta lisää lukuvinkkejä? (k/e): "
    END_BROWSING_TEXT = "\nLukuvinkkilistan selaaminen lopetettu."
    TIPS_PER_PAGE = 10
    REMOVAL_SUCCESS_TEXT = "Vinkin poisto onnistui."
    REMOVAL_FAIL_TEXT = "Vinkin poisto epäonnistui."
    REMOVAL_GREET = "Poistetaanko vinkkejä? (k/e): "
    CHOOSE_TIP_FOR_REMOVAL = "Syötä vinkin numero: "

    class MenuCommands:
        """ A short class for storing the menu commands.
        """
        STOP = "e"
        NEXT_PAGE = "k"

    def execute(self):
        list_of_tips = self._reading_tip_service.get_all_tips()
        self._io.write(self.GREET_TEXT)

        for tip_number, tip in enumerate(list_of_tips):
            user_tip_number = tip_number + 1
            self._io.write(f"{user_tip_number}: {tip.title}")

            if tip_number == len(list_of_tips) - 1:
                break

            if (tip_number + 1) % self.TIPS_PER_PAGE == 0:
                user_input = self._io.read(self.QUERY_FOR_MORE_TEXT)
                if user_input == self.MenuCommands.STOP:
                    break

        if not list_of_tips:
            return
        else:
            removal_input = self._io.read(self.REMOVAL_GREET)
            if removal_input == self.MenuCommands.STOP:
                return
            removal_number = int(self._io.read(self.CHOOSE_TIP_FOR_REMOVAL))

            if self._reading_tip_service.remove_reading_tip(list_of_tips[removal_number-1]):
                self._io.write(self.REMOVAL_SUCCESS_TEXT)
            else:
                self._io.write(self.REMOVAL_FAIL_TEXT)


class UnknownCommand(Command):
    """ Used as a default for non-existing commands.
    """
    UNKNOWN_COMMAND_TEXT = "Tuntematon syöte."

    def execute(self):
        self._io.write(self.UNKNOWN_COMMAND_TEXT)


class CommandFactory:
    """ A handling class for all the user commands recognized by the program. 
    """

    def __init__(self, io, reading_tip_service, commands=None):
        """ Inits the factory. Use commands-arg to inject different commands.
        """
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
        """ Returns the command corresponding to the user input or UnknownCommand when no
        such command exists.
        """
        return self._commands.get(command_string,
                                  UnknownCommand(self._io, self._reading_tip_service))
