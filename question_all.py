import json
from Class_Question import Question
from information import get_status
from authentification import get_authorization


def convert_dict(code: int, questions: list) -> dict:
    """Преобразование в словарь"""
    question_list = {"Category": code}
    for i in range(len(questions)):
        question_list[i + 1] = questions[i][0]
    return question_list


def get_questions(token: str) -> list or str:
    if get_authorization(token):
        status = get_status(token)
        if status == "Applicant":
            qq = Question()
            random_id = qq.rand()
            qq.give_random_id(random_id)
            questions = qq.choice_quest()
            code = qq.choice_code()
            return json.dumps(convert_dict(code, questions))
        else:
            return json.dumps("Отказано в доступе")
    else:
        return json.dumps("Вы не авторизованы")
