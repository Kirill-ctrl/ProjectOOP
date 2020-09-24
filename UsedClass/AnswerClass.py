from DBClass.DataBaseClass import AnswerTable


class Answer1:

    def __init__(self):
        self.db = AnswerTable()
        self.code = None
        self.list_quest_id = None
        self.key_answer_dict = None
        self.applicant_id = None
        self.list_id_questions = None

    def give_data_answer(self, code: int, key_answer_dict: list, list_id_questions: list) -> None:
        """Получаем информацию о пользователе"""
        self.code = code
        self.list_id_questions = list_id_questions
        self.key_answer_dict = key_answer_dict

    def give_applicant_id(self, applicant_id: int) -> None:
        """Получаем id соискателя"""
        self.applicant_id = applicant_id

    def insert_answer(self, applicant_id: int, value_answer_dict: list, question_id: list) -> None:
        """Добавляем ответы соискателя"""
        self.db.insert_answer_applicants(applicant_id, value_answer_dict, question_id)

    def check_answer(self) -> list:
        """Проверяем, есть ли уже ответы соискателя"""
        list_answer = self.db.check_answer_applicants(self.applicant_id)
        return list_answer

    def get_answer_list(self) -> tuple:
        """Получаем ответы (текст ответа и id вопросов) соискателя"""
        list_tuple = self.db.get_answer_list_applicants(self.applicant_id)

        text_answer = [list_tuple[i][1] for i in range(len(list_tuple))]

        id_questions = tuple([list_tuple[i][0] for i in range(len(list_tuple))])

        return text_answer, id_questions
