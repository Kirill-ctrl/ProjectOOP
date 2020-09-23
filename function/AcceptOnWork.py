from UsedClass.ApplicantClass import Applicant
from function.Information import get_status
import json
from function.Authentication import get_authorization
from UsedClass.EmployerClass import Employer


def accept_applicant(token: str, employer_email: str, applicant_email: str) -> str:
    if get_authorization(token):
        status = get_status(token)
        if status == "Applicant":
            return json.dumps('Отказано в доступе')
        else:
            employ = Employer()
            employer_id = employ.get_employer_id(employer_email)
            job_seeker = Applicant()
            job_seeker.accept_applicant(employer_id, applicant_email)
            return json.dumps('Успешно обновлено')
    else:
        return json.dumps("Вы не авторизованы")
