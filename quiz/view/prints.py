from termcolor2 import colored


class PrintStatements:
    """
    This class is for printing messages
    """
    @staticmethod
    def print_func(message, color='white'):
        print(colored(message, color=color))
