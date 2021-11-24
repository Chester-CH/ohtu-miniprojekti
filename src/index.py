from console_io import ConsoleIO


class LukuvinkkiApp:
    def __init__(self, io=None):
        if not io:
            io = ConsoleIO()
        self.io = io

    def run(self):
        self.io.write("Hello world!")


if __name__ == "__main__":
    app = LukuvinkkiApp()
    app.run()
