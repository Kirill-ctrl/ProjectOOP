from DBClass.DataBaseClass import ApplicantTable


class Applicant:

    def __init__(self):
        self.db = ApplicantTable()
        self.name = None
        self.email = None
        self.token = None
        self.status = None
        self.user_id = None
        self.applicant_id = None

    def give_information_applicant(self, name: str, email: str, token: str, status: str, users_id: int) -> None:
        """Получаем информацию о соискателе"""
        self.name = name
        self.email = email
        self.token = token
        self.status = status
        self.user_id = users_id

    def give_applicant_id(self, applicant_id: int) -> None:
        """Получаем id соискателя"""
        self.applicant_id = applicant_id

    def get_applicant_list(self) -> list:
        """Получаем список соискателей"""
        list_tuple = self.db.applicant_list()
        return list_tuple

    def update_cat(self, code: int) -> None:
        """Изменяем поле на значение категории вопросов, на которые ответил соискатель"""
        self.db.update_category_questions(code, self.email)

    def list_for_employers(self) -> list:
        """Получение данных по соискателям"""
        list_tuples = self.db.applicant_list_for_employers()
        return list_tuples

    def accept_applicant(self, employer_id: int, applicant_email: str):
        """Ставим соискателю id работодателя"""
        self.db.update_applicant_accepted(employer_id, applicant_email)

    def get_information_from_email(self, email: str) -> tuple:
        """Получаем информацию по email"""
        list_tuple = self.db.get_data_by_email(email)
        name = list_tuple[0][0]
        email = list_tuple[0][1]
        status = list_tuple[0][2]
        users_id = list_tuple[0][3]
        applicant_id = list_tuple[0][4]
        return name, email, status, users_id, applicant_id

    def add_new_applicant(self, name: str, city: str, age: int, email: str, users_id: int):
        """Добавляем нового соискателя"""
        self.db.new_applicant(name, city, age, email, users_id)
