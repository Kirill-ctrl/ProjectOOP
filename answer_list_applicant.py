from Class_Question import Question
from Class_Answer import Answer1
from Applicant_Class import Applicant
import json
from information import get_status
from authentification import get_authorization


def sort_ans_list(text_answer: list, text_question: list) -> list:
    """Преобразует в словарь """
    list_dict = [{'text_question': text_question[i], 'text_answer': text_answer[i]} for i in range(len(text_answer))]
    return list_dict


def get_list_answer_applicant(token: str, email: str) -> list or str:
    if get_authorization(token):
        status = get_status(token)
        if status == "Applicant":
            return json.dumps("Отказано в доступе")
        else:
            job_seeker = Applicant()
            name, email, status, users_id, applicant_id = job_seeker.get_information_from_email(email)
            job_seeker.give_applicant_id(applicant_id)

            ans = Answer1()
            ans.give_applicant_id(applicant_id)
            text_answer, id_question = ans.get_answer_list()

            qq = Question()
            text_question = qq.get_quest_text(id_question)

            list_dict = sort_ans_list(text_answer, text_question)
            return json.dumps(list_dict)
    else:
        return json.dumps("Вы не авторизованы")
