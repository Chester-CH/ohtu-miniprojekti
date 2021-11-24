class MockIO:
    def __init__(self, input_list=None):
        if not input_list:
            input_list = []
        self.input_list = input_list
        self.output_list = []

    def read(self, input_prompt=None):
        try:
            return self.input_list.pop(0)
        except IndexError:
            return ""

    def write(self, message):
        self.output_list.append(message)
