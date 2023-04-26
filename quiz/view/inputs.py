from hashlib import sha512
from getpass import getpass

from conf import Settings
from termcolor2 import colored
from .clear_screen import ClearScreen

class InputStatement:
    """
"This class provides inputs for the program.
Its methods are designed to get input from the user in specific situations."
    """
    @staticmethod
    def empty_input():
        input()

    @staticmethod
    def show_message(message, color,):
        ClearScreen.clear_screen()
        getpass(colored(message, color=color))
        
    @staticmethod
    def input_func(message, color, clear=True):
        if clear is True:
            ClearScreen.clear_screen()
        result = input(colored(message, color=color))
        return result

    @staticmethod
    def login_or_register():
        register_statement = colored(
            "\n\nPress 1 to register\n\n",
            color="red"
            )
        login_statement = colored(
            "\n\nPress 2 to login\n\n",
            color='green'
            )
        ClearScreen.clear_screen()
        login_register = input(f'{register_statement}{login_statement}')
        return login_register

    @staticmethod
    def register_input_username():
        statement = colored(
            "\n\nPlease Enter your username to register: ", "light_green"
            )
        ClearScreen.clear_screen()
        username = input(statement)
        return username

    @staticmethod
    def login_input_username():
        statement = colored(
            "\n\nPlease Enter your username to login: ", "light_green"
            )
        ClearScreen.clear_screen()
        username = input(statement)
        return username

    @staticmethod
    def input_password():
        statement = colored(
            "\n\nPlease Enter your password: ",
            color="light_green"
            )
        ClearScreen.clear_screen()
        password = getpass(statement)
        return password
    
    @staticmethod
    def want_superuser():
        statement = colored(
            "\n\nDo you want to register as a superuser? [y/n]",
            color="light_green"
            )
        ClearScreen.clear_screen()
        superuser = input(statement).lower()
        status = False
        if superuser == "y":
            status = True
        return status
    
    @staticmethod
    def input_security_code():
        statement = colored(
            "\nPlease Enter the code: ",
            color="red"
            )
        ClearScreen.clear_screen()
        security_code = input(statement)
        hashed_code = (sha512(security_code.encode())).hexdigest()
        return hashed_code

            
    @staticmethod
    def input_question():
        statement = colored(
            "\n\nPlease Enter the question that you want to insert in database: ",
            color="light_green"
            )
        ClearScreen.clear_screen()
        question = input(statement)
        return question
    
    @staticmethod
    def input_question_answers():
        options = ["a)", "b)", "c)", "d)"]
        statement = colored(
            "\n\nPlease enter the options in order to add the answers to the database.",
            color="light_green"
            )
        answers = dict()
        for option in options:
            print(statement)
            input_statement = colored(
                f"\n{option}is: ",
                color="magenta"
                )
            ClearScreen.clear_screen()
            answer = input(input_statement)
            answers[option] = answer
        return answers

    @staticmethod
    def input_correct_answer():
        statement = colored(
            "\n\nPlease Enter the correct answer: ",
            color="light_green"
            )
        ClearScreen.clear_screen()
        correct_answer = input(statement)
        return correct_answer
    
    @staticmethod
    def get_answer():
        statement = colored(
            "\nPlease select of the options: ",
            color="light_green"
            )
        answer = input(statement)
        return answer