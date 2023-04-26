from quiz.models import Question
from quiz.view import ClearScreen
from helper.messages import Message
from quiz.presenter.take_quiz import Quiz
from quiz.view import(
    InputStatement,
    PrintStatements
)
from quiz.presenter.question_management import QuestionManagement


class AdminPanel:
    """
Enhanced Paragraph:
"This class is designed for managing the admin panel.
Only superusers have access to the admin panel.
This class provides additional options for users, such as viewing, adding,
or deleting questions."
    """
    @classmethod
    def create_panel(cls):
        admin = True
        while admin is True:
            choice = InputStatement.input_func(
                Message.admin_choice,
                color="magenta"
                )
            panel = True
            if choice == "q":
                break
            elif choice == "1":
                while panel is True:
                        select_options = InputStatement.input_func(
                            Message.select_option,
                            color="cyan"
                            )
                        if select_options == "p":
                            panel = False
                        elif select_options == "q":
                            panel = False
                            admin = False
                        elif select_options == "1":
                            ClearScreen.clear_screen()
                            QuestionManagement.read_questions()
                            InputStatement.empty_input()
                        elif select_options == "2":
                            QuestionManagement.insert_question()
                        elif select_options == "3":
                            ClearScreen.clear_screen()
                            QuestionManagement.read_questions()
                            id = InputStatement.input_func(
                                Message.delete_question_id,
                                color="red",
                                clear=False
                                )
                            QuestionManagement.delete_question(id)
                            InputStatement.empty_input()
            elif choice == "2":
                Quiz.take_quiz()