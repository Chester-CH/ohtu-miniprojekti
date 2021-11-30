from services.reading_tip_service import reading_tip_service as default_reading_tip_service
from console_io import default_console


class UI:
    _greet_text = "Hei, tervetuloa Lukuvinkki sovellukseen\n"
    _menu_text = "\nAnna komento:\n1: lisää lukuvinkki\n0: lopeta"

    def __init__(self, io=default_console, reading_tip_service=default_reading_tip_service):
        self._io = io
        self._reading_tip_service = reading_tip_service

    def _add_new_title(self):
        inputTitle = self._io.read("Kirjoita otsikko: ")
        reading_tip = self._reading_tip_service.create_reading_tip(inputTitle)
        if reading_tip is not None:
            return True
        return False

    def start(self):
        self._io.write(self._greet_text)

        while True:
            self._io.write(self._menu_text)

            inputFeature = self._io.read("Syötä tominta: ")
            if inputFeature == "0":
                break
            if inputFeature == "1":
                self._add_new_title()


default_ui = UI()
