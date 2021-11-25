class ConsoleIO:
    """ A class for handling console IO. Used when interacting with actual users.
    """

    @staticmethod
    def read(input_prompt):
        """ Prints the input_prompt to the user and waits for input. Returns user input.
        """
        return input(input_prompt)

    @staticmethod
    def write(message):
        """ Prints the given message to the console.
        """
        print(message)
