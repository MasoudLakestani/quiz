from random import sample

from conf import Settings
from quiz.models import Question
from helper.messages import Message
from quiz.view import PrintStatements
from quiz.view import(
    ClearScreen,
    InputStatement,
    PrintStatements
) 
from quiz.presenter.check import CheckSatus


class QuestionManagement:
    """
This class is responsible for managing questions in the database.
Its methods include reading, inserting, and deleting questions from the database
    """
    @staticmethod
    def read_questions():
        questions = Question.read()
        for question in questions:
            question, = question
            message = f"{question.id}\t{question.question}"
            PrintStatements.print_func(message)

    @staticmethod
    def insert_question():
        input_questions = InputStatement.input_question()
        input_answers = InputStatement.input_question_answers()
        input_correct_answer = InputStatement.input_correct_answer()
        Question.create(
            input_questions,
            input_answers,
            input_correct_answer
            )
        PrintStatements.print_func(Message.successful_add, "blue")
    
    @staticmethod
    def delete_question(id):
        Question.delete(id=id)
        PrintStatements.print_func(Message.delete_question)

    staticmethod
    def choice_random_questions():
        questions = Question.read()
        selected_questions = sample(questions, Settings.number_of_questions)
        return selected_questions


