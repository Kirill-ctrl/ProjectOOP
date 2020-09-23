from UsedClass.QuestionClass import Question
from UsedClass.AnswerClass import Answer1
from UsedClass.ApplicantClass import Applicant
import json
from function.Information import get_status
from function.Authentication import get_authorization


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
            text_answer, id_questions = ans.get_answer_list()  # Получаем текст ответа и id вопросов, на которые отвечал соискатель

            qq = Question()
            text_question = qq.get_quest_text(id_questions)  # Получаем текст вопросов по id

            list_dict = sort_ans_list(text_answer, text_question)  # Сортируем по тексту вопроса и ответу на него
            return json.dumps(list_dict)
    else:
        return json.dumps("Вы не авторизованы")
