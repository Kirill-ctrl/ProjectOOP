import json
from Applicant_Class import Applicant
from Class_Question import Question
from information_applicant import get_information_applicant
from Class_Answer import Answer1
from information import get_status
from authentification import get_authorization


def insert_answer_applicant(list_answer_applicant: list, code: int, token: str) -> str:
    if get_authorization(token):
        status = get_status(token)
        if status == "Applicant":
            key_answer_dict = []
            for key in list_answer_applicant:
                key_answer_dict.append(list_answer_applicant[key])
            name, email, status, users_id, applicant_id = get_information_applicant(token)

            job_seeker = Applicant()
            job_seeker.give_information_applicant(name, email, token, status, users_id)
            job_seeker.give_applicant_id(applicant_id)
            job_seeker.update_cat(code)

            qq = Question()
            list_quest_id = qq.id_quest(code)

            ans = Answer1()
            ans.give_data_answer(code, key_answer_dict, list_quest_id)
            ans.give_applicant_id(applicant_id)

            list_answer = ans.check_answer()
            if list_answer:
                return json.dumps('Ответы уже добавлены')
            else:
                ans.update_answer()
                return json.dumps('Добавлено')
        else:
            return json.dumps('Отказано в доступе')
    else:
        return json.dumps("Вы не авторизованы")
