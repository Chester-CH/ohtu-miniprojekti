from ui.base_command import Command, QuitSignal
from ui.command_factory import CommandFactory
from ui.tip_printer import TipPrinter

class BrowseMenuCommands:
    """ Menu commands for browsing tips. """
    YES = "k"
    NO = "e"
    SHOW_MORE_TIPS = "t"
    STOP_BROWSING = "l"
    REMOVE_TIP = "p"


class BrowseTips(Command):
    """ Command for browsing the created tips list.
    """
    GREET_TEXT = "\nSelaa lukuvinkkejä:"
    COMMAND_HELP_TEXT = "Komennot: 0: lopeta, 1: Seuraava sivu"
    QUERY_FOR_MORE_TEXT = "(t)ulosta lisää vinkkejä, (p)oista vinkki tai (l)opeta selaus: "
    QUERY_AT_END_TEXT = "(p)oista vinkki tai (l)opeta selaus: "
    END_BROWSING_TEXT = "\nLukuvinkkilistan selaaminen lopetettu."
    NO_TIPS_FOUND_TEXT = "Lukuvinkkejä ei löytynyt."
    TIPS_PER_PAGE = 10

    def __init__(self, io, reading_tip_service):
        super().__init__(io, reading_tip_service)
        self._command_factory = None

    def _init_commands(self, tip_list):
        menu_commands = {
            BrowseMenuCommands.REMOVE_TIP:
            RemoveTip(self._io, self._reading_tip_service, tip_list),
            BrowseMenuCommands.STOP_BROWSING:
            StopBrowsing(self._io, self._reading_tip_service),
            BrowseMenuCommands.SHOW_MORE_TIPS:
            ShowMoreTips(self._io, self._reading_tip_service),
        }
        self._command_factory = CommandFactory(
            self._io, self._reading_tip_service, menu_commands)

    def _handle_input(self, query_text, tip_list):
        try:
            while not all(tip is None for tip in tip_list):
                user_input = self._io.read(query_text).lower()
                self._command_factory.get_command(user_input).execute()
            return BrowseMenuCommands.STOP_BROWSING
        except QuitSignal as quit_signal:
            return str(quit_signal)

    def execute(self):
        """ Shows the browse tips menu and handles all UI-related tasks. """
        tip_list = self._reading_tip_service.get_all_tips()
        self._init_commands(tip_list)
        self._io.write(self.GREET_TEXT)

        if not tip_list:
            self._io.write(self.NO_TIPS_FOUND_TEXT)
            return

        tip_number = 0
        while tip_number < len(tip_list):
            user_tip_number = tip_number + 1
            tip = tip_list[tip_number]
            self._io.write(
                f"{user_tip_number}: {TipPrinter.get_description(tip)}")

            if tip_number == len(tip_list) - 1:
                break

            if (tip_number + 1) % self.TIPS_PER_PAGE == 0:
                if (self._handle_input(self.QUERY_FOR_MORE_TEXT, tip_list)
                        == BrowseMenuCommands.STOP_BROWSING):
                    return

            tip_number += 1

        if self._reading_tip_service.get_all_tips():
            self._handle_input(self.QUERY_AT_END_TEXT, tip_list)


class RemoveTip(Command):
    """ A command for removing a single tip from a tip list. """

    REMOVAL_SUCCESS_TEXT = "Vinkin poisto onnistui."
    REMOVAL_FAIL_TEXT = "Vinkin poisto epäonnistui."
    CHOOSE_TIP_FOR_REMOVAL = "Syötä vinkin numero: "
    BAD_TIP_NUMBER = "Virheellinen numero."

    def __init__(self, io, reading_tip_service, tip_list):
        super().__init__(io, reading_tip_service)
        self._tip_list = tip_list

    def execute(self):
        """ Handles the remove tip part of the browse tips menu. """
        try:
            removal_number = int(self._io.read(self.CHOOSE_TIP_FOR_REMOVAL))
        except ValueError:
            self._io.write(self.BAD_TIP_NUMBER)
            return

        if removal_number < 1 or removal_number > len(self._tip_list):
            self._io.write(self.BAD_TIP_NUMBER)
            return

        selected_tip = self._tip_list[removal_number - 1]

        if self._reading_tip_service.remove_reading_tip(selected_tip):
            self._io.write(self.REMOVAL_SUCCESS_TEXT)
            self._tip_list[removal_number - 1] = None
        else:
            self._io.write(self.REMOVAL_FAIL_TEXT)


class ShowMoreTips(Command):
    """ Used when the user wants to be shown more tips in the browse menu. """
    def execute(self):
        """ Raises a quit signal. """
        # pylint: disable=no-self-use
        raise QuitSignal(BrowseMenuCommands.SHOW_MORE_TIPS)


class StopBrowsing(Command):
    """ Used when the user wants to quit browsing tips. """
    def execute(self):
        """ Raises a quit signal. """
        # pylint: disable=no-self-use
        raise QuitSignal(BrowseMenuCommands.STOP_BROWSING)
