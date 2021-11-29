from console_io import ConsoleIO
from reading_tip_app import ReadingTipApp
from ui.ui import UI

if __name__ == "__main__":
    app = ReadingTipApp(UI(ConsoleIO()))
    app.run()
