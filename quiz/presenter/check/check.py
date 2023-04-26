from quiz import models
from conf import Settings
from helper import exceptions as exc


class CheckSatus:
    """
    "This class serves as a validator, checking for correct formats in
    usernames, passwords, and user-inserted answers." 
    """
    @staticmethod
    def check_username(get_username):
        username = models.User.read(get_username)
        if username is not None:
            raise exc.SameUserNameError()
        if len(get_username) < 5:
            raise exc.UsernameLengthError()
        if not get_username[0].isalpha():
            raise exc.WrongUserNameError()
        return get_username

    @staticmethod
    def check_password(get_password):
        if len(get_password) < 8:
            raise exc.PasswordLengthError()
        if get_password.isalpha() or get_password.isdigit():
            raise exc.WrongPasswordError()
        return get_password 
    
    @staticmethod
    def check_valid_answer(get_answer):
        if get_answer not in Settings.valid_answers:
            raise exc.WrongAnswerFormat()
        return get_answer

