class UnknownCommand:
    """ Used as a default for non-existing commands.
    """
    UNKNOWN_COMMAND_TEXT = "Tuntematon syöte."

    def __init__(self, io):
        self._io = io

    def execute(self):
        """ Called when the user gives an unknown command. """
        self._io.write(self.UNKNOWN_COMMAND_TEXT)


class CommandFactory:
    """ A handling class for all the user commands recognized by the program.
    """

    def __init__(self, io, reading_tip_service, commands):
        """ Inits the factory. Use commands-arg to inject different commands.
        """
        self._io = io
        self._reading_tip_service = reading_tip_service
        self._commands = commands

    def get_command(self, command_string):
        """ Returns the command corresponding to the user input or UnknownCommand when no
        such command exists.
        """
        return self._commands.get(command_string, UnknownCommand(self._io))
