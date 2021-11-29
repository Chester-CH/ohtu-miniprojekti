from services.reading_tip_service import (
    reading_tip_service as default_reading_tip_service 
)

class UI:
    def __init__(
        self, 
        io,
        reading_tip_service = default_reading_tip_service
        ):
        self._io = io
        self._reading_tip_service = reading_tip_service
    
    def _add_new_title(self):
        inputTitle = self._io.read("Kirjoita otsikko: ")
        reading_tip = self._reading_tip_service.create_reading_tip(inputTitle)
        if reading_tip is not None:
            return True
        return False


    def start(self):
        while True:
            self._io.write("Hei, tervetuloa")
            self._io.write("1: lisää kirjaa")
            self._io.write("0: lopettaa")
            
            inputFeature = int(self._io.read("Syötä tominta: "))
            if inputFeature == 0:
                break
            if inputFeature == 1:
                self._add_new_title()

            
