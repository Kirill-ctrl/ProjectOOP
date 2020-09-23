import json
from UsedClass.QuestionClass import Question, QuestionList
from function.Information import get_status
from function.Authentication import get_authorization


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
            question_list = QuestionList()
            random_id = question_list.rand()
            qq.give_random_id(random_id)
            questions = qq.choice_quest()
            code = question_list.choice_code(random_id)
            return json.dumps(convert_dict(code, questions))
        else:
            return json.dumps("Отказано в доступе")
    else:
        return json.dumps("Вы не авторизованы")
