from conf import Settings
from quiz.models import User
from quiz.presenter.check import CheckSatus
from quiz.view import(
    ClearScreen,
    InputStatement,
    PrintStatements
) 
from helper import(
    exceptions as exc,
    Message
)


class Authentication:
    """
"This class manages the authentication process,
handling the registration and login procedures."
    """
    @classmethod
    def login_register(cls):
        InputStatement.show_message(
            Message.welcome_message,
            color="cyan",

            )
        selection = InputStatement.login_or_register()
        if selection == "1":
            cls.register()
            InputStatement.show_message(
                Message.need_to_login,
                color='magenta'
                )
            user = cls.login()
        if selection == "2":
            user = cls.login()
        return user

    @staticmethod
    def register():
        register_status = False
        username = password = None
        while register_status is False:
            try:
                if username is None:
                    input_user = InputStatement.register_input_username()
                    username = CheckSatus.check_username(input_user)
                if password is None:
                    input_user = InputStatement.input_password()
                    password = CheckSatus.check_password(input_user)
                want_to_superuser = InputStatement.want_superuser()
                is_superuser = False
                if want_to_superuser == True:
                    InputStatement.show_message(
                        Message.super_user_message,
                        color="red")
                    num = 0
                    while num < 3 and is_superuser is False:
                        security_code = InputStatement.input_security_code()
                        num += 1
                        if security_code == Settings.hashed_code:
                            is_superuser = True
                        else:
                            InputStatement.show_message(
                                Message.success_message(num),
                                color="red"
                                )
                            ClearScreen.clear_screen() 
                User.create(
                    username,
                    password,
                    is_superuser
                    )
                register_status = True
                return register_status
                InputStatement.empty_input()
            except exc.UsernameLengthError as e:
                InputStatement.show_message(e, color='red')
            except exc.WrongUserNameError as e:
                InputStatement.show_message(e, color='red')
            except exc.SameUserNameError as e:
                InputStatement.show_message(e, color='red')
            except exc.PasswordLengthError as e:
                InputStatement.show_message(e, color='red')
            except exc.WrongPasswordError as e:
                InputStatement.show_message(e, color='red')

    @staticmethod
    def login():
        login_status = False
        while login_status is False:
            get_username = InputStatement.login_input_username()
            get_password = InputStatement.input_password()
            user = User.read(get_username)
            if user is not None:
                user = user[0]
                if user.password == get_password:
                    login_status = True
                    logged_in_user = user
            if login_status is False:
                InputStatement.show_message(
                    Message.login_error,
                    color='red'
                    )
        ClearScreen.clear_screen()
        PrintStatements.print_func('\n')
        return logged_in_user

