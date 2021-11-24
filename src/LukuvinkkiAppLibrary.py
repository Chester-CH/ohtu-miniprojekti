from mock_io import MockIO
from index import LukuvinkkiApp


class LukuvinkkiAppLibrary:
    def __init__(self):
        self.io = MockIO()
        self.app = LukuvinkkiApp(self.io)

    def output_should_contain(self, message):
        if not message in self.io.output_list:
            raise AssertionError(
                f"Missing output \"{message}\" in {str(self.io.output_list)}")

    def run_application(self):
        self.app.run()
