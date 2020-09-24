from UsedClass.ApplicantClass import Applicant
from UsedClass.QuestionClass import Question
from function.InformationApplicant import get_information_applicant
from UsedClass.AnswerClass import Answer1
from function.Information import get_status
from function.Authentication import get_authorization
from function.response import answers_already_added, not_authorized, access_denied, added
from function.get_check_status import check_status_applicant


def insert_answer_applicant(list_answer_applicant: list, token: str, code: int) -> str:
    """Добавляем ответы соискателя"""
    if get_authorization(token):
        status = get_status(token)
        if check_status_applicant(status):

            value_answer_dict = []
            for key in list_answer_applicant:
                value_answer_dict.append(list_answer_applicant[key])

            key_answer_pseudonym = []
            for key in list_answer_applicant:
                key_answer_pseudonym.append(key)

            name, email, status, users_id, applicant_id = get_information_applicant(token)

            answer = Answer1()
            answer.give_applicant_id(applicant_id)

            list_answer = answer.check_answer()

            if list_answer:

                return answers_already_added()

            else:

                question = Question()
                list_tuple = question.get_id_and_pseudonym(key_answer_pseudonym)

                question_id = []
                for i in range(len(list_tuple)):
                    question_id.append(list_tuple[i])

                answer.insert_answer(applicant_id, value_answer_dict, question_id)

                job_seeker = Applicant()
                job_seeker.give_information_applicant(name, email, token, status, users_id)
                job_seeker.give_applicant_id(applicant_id)
                job_seeker.update_cat(code)

                return added()
        else:
            return access_denied()
    else:
        return not_authorized()
