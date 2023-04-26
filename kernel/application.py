from quiz.presenter.take_quiz import Quiz 
from quiz.presenter.auth import Authentication
from quiz.presenter.admin_panel import AdminPanel

def main():
    user = Authentication.login_register()
    if user.is_superuser is False:
        Quiz.take_quiz()
    else:
        AdminPanel.create_panel()



