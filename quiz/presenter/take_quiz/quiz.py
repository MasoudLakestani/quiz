from conf import Settings
from quiz.view import ClearScreen
from quiz.models import User, Question
from quiz.presenter.check import CheckSatus
from quiz.view.inputs import InputStatement
from quiz.view.prints import PrintStatements
from helper import(
    exceptions as exc,
    Message
)
from quiz.presenter.question_management import QuestionManagement


class Quiz:
    """
"This class is responsible for conducting quizzes. It selects questions,
checks if users' answers are correct or not, and calculates the users' scores."
    """
    @staticmethod
    def take_quiz():
        selected_questions = QuestionManagement.choice_random_questions()
        InputStatement.show_message(Message.start_exam, "yellow")
        score = 0
        ClearScreen.clear_screen()
        for question in selected_questions:
            question, = question
            answer_format = False
            while answer_format is False:
                PrintStatements.print_func(question, "magenta") 
                shown_answers = "\n"
                for key, value in question.answers.items():
                    shown_answers += f"{key}{value}\t\t"
                PrintStatements.print_func(shown_answers, "red")
                input_answer = InputStatement.get_answer()
                try:
                    CheckSatus.check_valid_answer(input_answer)
                    answer_format = True
                except exc.WrongAnswerFormat as e:
                    ClearScreen.clear_screen()
                    InputStatement.show_message(e, color='red')
                    ClearScreen.clear_screen()           
            if input_answer == question.correct_answer:
                score += 20
            ClearScreen.clear_screen()
            message = f"\n\nYou answered {score//20} questions correctly"\
                        f" and your score is {score}"
        PrintStatements.print_func(message, "red")
        InputStatement.empty_input()
            

