from UsedClass.EmployerClass import Employer
from function.Information import get_status
import json
from function.Authentication import get_authorization


def convert_employer(list_tuple: list) -> list:
    list_dict = [{"name": list_tuple[i][0], "city": list_tuple[i][1]} for i in range(len(list_tuple))]
    return list_dict


def get_inf_employer(token: str) -> list or str:
    if get_authorization(token):
        status = get_status(token)
        if status == "Applicant":
            list_tuple = Employer().get_employer_list()
            return json.dumps(convert_employer(list_tuple))
        else:
            return json.dumps('Отказано в доступе')
    else:
        return json.dumps("Вы не авторизованы")
