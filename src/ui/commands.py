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
    FIELD_EMPTY_TEXT = "Syöte ei voi olla tyhjä."
    ADD_TYPE_TEXT = "Syötä tyyppi: "
    BAD_TYPE_NUMBER = "Virheellinen syöte"
    ADD_AUTHOR = "Syötä tekijä: "
    ADD_ISBN = "Syötä ISBN numero: "
    ADD_URL = "Syötä verkko-osoite: "
    ADD_NAME = "Syötä nimi: "
    ADD_DESCRIPTION = "Syötä kuvaus (vapaaehtoinen): "

    def __init__(self, io, reading_tip_service):
        super().__init__(io, reading_tip_service)
        self.handle_tip_input = {
            TipTypes.BOOK: self._fill_book_fields,
            TipTypes.BLOGPOST: self._fill_blogpost_fields,
            TipTypes.VIDEO: self._fill_video_fields,
            TipTypes.PODCAST: self._fill_podcast_fields
        }

    def _prompt_user(self, reading_tip, content_type, prompt_message, fail_message=None):
        if not fail_message:
            fail_message = self.FIELD_EMPTY_TEXT
        while True:
            value = self._io.read(prompt_message).strip()
            if reading_tip.try_set(content_type, value):
                return
            else:
                # This is only called if the validator fails.
                self._io.write(fail_message)

    def _fill_book_fields(self, reading_tip):
        self._prompt_user(reading_tip, "author", self.ADD_AUTHOR)
        self._prompt_user(reading_tip, "isbn", self.ADD_ISBN)

    def _fill_blogpost_fields(self, reading_tip):
        self._prompt_user(reading_tip, "url", self.ADD_URL)
        self._prompt_user(reading_tip, "author", self.ADD_AUTHOR)

    def _fill_video_fields(self, reading_tip):
        self._prompt_user(reading_tip, "url", self.ADD_URL)

    def _fill_podcast_fields(self, reading_tip):
        self._prompt_user(reading_tip, "url", self.ADD_URL)
        self._prompt_user(reading_tip, "author", self.ADD_AUTHOR)
        self._prompt_user(reading_tip, "name", self.ADD_NAME)

    def execute(self):
        tips_type = self._select_tips_type()
        if not tips_type:
            return
        reading_tip = ReadingTipFactory.get_new_reading_tip(tips_type)

        self._prompt_user(reading_tip, "title",
                          self.ADD_NEW_TIP_TEXT)
        self.handle_tip_input[tips_type](reading_tip)
        self._prompt_user(reading_tip, "description",
                          self.ADD_DESCRIPTION)

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
            if type_input == "":
                return None
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
