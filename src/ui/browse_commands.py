from ui.base_command import Command
from ui.command_factory import CommandFactory


class BrowseMenuCommands:
    YES = "k"
    NO = "e"
    BROWSE_MORE = "t"
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
    TIPS_PER_PAGE = 10

    def _init_commands(self, tip_list):
        menu_commands = {
            BrowseMenuCommands.REMOVE_TIP: RemoveTips(
                self._io, self._reading_tip_service, tip_list)
        }
        self._command_factory = CommandFactory(
            self._io, self._reading_tip_service, menu_commands)

    def _handle_input(self, query_text):
        while True:
            user_input = self._io.read(query_text).lower()

            if user_input == BrowseMenuCommands.STOP_BROWSING:
                return BrowseMenuCommands.STOP_BROWSING
            if user_input == BrowseMenuCommands.BROWSE_MORE:
                return BrowseMenuCommands.BROWSE_MORE
            self._command_factory.get_command(user_input).execute()

    def execute(self):
        tip_list = self._reading_tip_service.get_all_tips()
        self._init_commands(tip_list)
        self._io.write(self.GREET_TEXT)

        tip_number = 0
        while tip_number < len(tip_list):
            user_tip_number = tip_number + 1
            tip = tip_list[tip_number]
            self._io.write(f"{user_tip_number}: {tip.title}")

            if tip_number == len(tip_list) - 1:
                break

            if (tip_number + 1) % self.TIPS_PER_PAGE == 0:
                if self._handle_input(self.QUERY_FOR_MORE_TEXT) == BrowseMenuCommands.STOP_BROWSING:
                    return

            tip_number += 1

        self._handle_input(self.QUERY_AT_END_TEXT)


class RemoveTips(Command):
    REMOVAL_SUCCESS_TEXT = "Vinkin poisto onnistui."
    REMOVAL_FAIL_TEXT = "Vinkin poisto epäonnistui."
    CHOOSE_TIP_FOR_REMOVAL = "Syötä vinkin numero: "
    BAD_TIP_NUMBER = "Virheellinen numero."

    def __init__(self, io, reading_tip_service, tip_list):
        super().__init__(io, reading_tip_service)
        self._tip_list = tip_list

    def execute(self):
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
        else:
            self._io.write(self.REMOVAL_FAIL_TEXT)
