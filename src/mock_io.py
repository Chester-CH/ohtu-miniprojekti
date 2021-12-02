class MockIO:
    """ Stub class for IO operation testing.
    """

    def __init__(self, input_list=None):
        if not input_list:
            input_list = []
        self.input_list = input_list
        self.output_list = []

    def read(self, input_prompt=None):
        """ Returns the first string on the input list, or an empty string if the list is empty.
        """
        # pylint: disable=unused-argument
        try:
            self.write(input_prompt)
            return self.input_list.pop(0)
        except IndexError:
            return ""

    def write(self, message):
        """ Writes the message to the end of the output list.
        """
        self.output_list.append(message)
