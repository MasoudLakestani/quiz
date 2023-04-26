from termcolor2 import colored
from conf import Settings


class Message:
    welcome_message = "*****************************************************************\n" \
    "*\t    Are you ready to challenge your knowledge?\t        *\n" \
    "*          \tSo, wait no more and sign up.\t                *\n"\
    "* Please note that in order to sign up as an admin (superuser), *\n"\
    "*\t\tyou must enter the security code.\t\t*\n"\
    "*  \tDon't worry if you don't have a security code,\t\t*\n"\
    "*  you can still sign up as a regular user and enjoy the quiz.  *\n"\
    "*****************************************************************\n" 
    login_error = '\nThe username or password are not correct. Please try again '
    need_to_login = '\n\ncongratulation you registered successfully!\n\nNow you have to login\n\nPlease Press Enter to continue...'
    exit_messages = ['quit', 'exit', 'q', 'stop']
    successful_add= "\nThe question has been successfully added to the database."
    start_exam = "\n\nAre you ready for the quiz? "
    super_user_message =  "\n\nTo register as a superuser, you need to provide the security code.\nNote that you have three opportunities to enter the correct code."
    admin_choice = "\n\nPlease select an option: Press 1 to access the admin panel or press 2 to test yourself.\n"\
        "At any stage, you can return to the previous menu by entering 'p' and exit the program by entering 'q'.\n"
    select_option = "\n\nPlease choose one of the following options"\
        "\nPress 1 if you want to see questions"\
        "\nPress 2 if you want insert a questions to database "\
        "\nPress 3 if you want to delete questions\n"
    delete_question = "The question has been successfully deleted"
    delete_question_id = "Please input the ID of the question that you would like to delete."
    
    @staticmethod
    def success_message(num):
        if 3 - num != 0:
            message = "It appears that you may have inputted an incorrect code\n"\
                f"Please note that you are allowed only {3 - num} attempts to enter the security code for superuser registration"
        else:
            message = "Unfortunately, your chance to register as a superuser has expired.\n"\
                "Your registration has been processed as a regular user."
        return message