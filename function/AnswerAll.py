import json
from UsedClass.ApplicantClass import Applicant
from UsedClass.QuestionClass import Question
from function.InformationApplicant import get_information_applicant
from UsedClass.AnswerClass import Answer1
from function.Information import get_status
from function.Authentication import get_authorization


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
            job_seeker.update_cat(code)  # Ставим соискателю категорию вопросов, на которые ответил

            qq = Question()
            list_id_questions = qq.id_quest(code)  # Выбираем id вопросов, на которые отвечал соискатель по коду -> список

            ans = Answer1()
            ans.give_data_answer(code, key_answer_dict, list_id_questions)  # Передаем код, ответы соискателя, и id вопросов, на которые отвечал соискатель
            ans.give_applicant_id(applicant_id)

            list_answer = ans.check_answer()
            if list_answer:
                return json.dumps('Ответы уже добавлены')
            else:
                ans.insert_answer()  # Добавляем ответы соискателя в таблицу answer
                return json.dumps('Добавлено')
        else:
            return json.dumps('Отказано в доступе')
    else:
        return json.dumps("Вы не авторизованы")
