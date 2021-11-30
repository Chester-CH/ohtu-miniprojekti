from services.reading_tip_service import reading_tip_service as default_reading_tip_service
from console_io import default_console


class UI:
    GREET_TEXT = "Hei, tervetuloa Lukuvinkki sovellukseen"
    MENU_TEXT = "\nAnna komento:\n1: lisää lukuvinkki\n0: lopeta"
    ADDITION_SUCCESS_TEXT = "Uuden lukuvinkin luonti onnistui."
    ADDITION_FAIL_TEXT = "Uuden lukuvinkin luonti epäonnistui."

    def __init__(self, io=default_console, reading_tip_service=default_reading_tip_service):
        self._io = io
        self._reading_tip_service = reading_tip_service

    def _add_new_title(self):
        inputTitle = self._io.read("Kirjoita otsikko: ")
        reading_tip = self._reading_tip_service.create_reading_tip(inputTitle)
        if reading_tip is not None:
            self._io.write(self.ADDITION_SUCCESS_TEXT)
        else:
            self._io.write(self.ADDITION_FAIL_TEXT)

    def start(self):
        self._io.write(self.GREET_TEXT)

        while True:
            self._io.write(self.MENU_TEXT)

            inputFeature = self._io.read("Syötä tominta: ")
            if inputFeature == "0":
                break
            if inputFeature == "1":
                self._add_new_title()


default_ui = UI()
