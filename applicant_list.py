from Applicant_Class import Applicant
import json
from information import get_status
from authentification import get_authorization


def convert_applicant(list_tuple: list) -> list:
    """Преобразуем, работает c соискателями"""
    list_dict = []
    for i in range(len(list_tuple)):
        list_dict.append({
            "id": list_tuple[i][0],
            "name": list_tuple[i][1],
            "city": list_tuple[i][2],
            "age": list_tuple[i][3],
            "email": list_tuple[i][4],
            "question_list": list_tuple[i][5],
            "employer_id": list_tuple[i][6],
            "accept": list_tuple[i][7]
        })
    return list_dict


def get_inf_applicant(token: str) -> list or str:
    if get_authorization(token):
        status = get_status(token)
        if status == "Applicant":
            return json.dumps('Отказано в доступе')
        else:
            job_seeker = Applicant()
            list_tuple = job_seeker.get_applicant_list()
            return json.dumps(convert_applicant(list_tuple))
    else:
        return json.dumps("Вы не авторизованы")


def convert_applicant_list_for_employer(list_tuples: list) -> list:
    """Преобразовать список в словарь"""
    list_dicts = []
    for i in range(len(list_tuples)):
        list_dicts.append({
            "name": list_tuples[i][0],
            "city": list_tuples[i][1],
            "age": list_tuples[i][2],
            "email": list_tuples[i][3],
            "question_code": list_tuples[i][4]
        })
    return list_dicts


def get_applicant_list_for_employer(token: str) -> list or str:
    if get_authorization(token):
        status = get_status(token)
        if status == "Applicant":
            return json.dumps('Отказано в доступе')
        else:
            job_seeker = Applicant()
            list_tuples = job_seeker.list_for_employers()
            applicant_list = convert_applicant_list_for_employer(list_tuples)
            return json.dumps(applicant_list)
    else:
        return json.dumps("Вы не авторизованы")
