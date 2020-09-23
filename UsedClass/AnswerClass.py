from DBClass.DataBaseClass import AnswerTable


class Answer1:

    def __init__(self):
        self.db = AnswerTable()
        self.code = None
        self.list_quest_id = None
        self.key_answer_dict = None
        self.applicant_id = None
        self.list_id_questions = None

    def give_data_answer(self, code: int, key_answer_dict: list, list_id_questions: list):
        self.code = code
        self.list_id_questions = list_id_questions
        self.key_answer_dict = key_answer_dict

    def give_applicant_id(self, applicant_id: int):
        self.applicant_id = applicant_id

    def insert_answer(self):
        """Добавляем ответы в таблицу answer"""
        self.db.insert_answer_applicants(self.applicant_id, self.key_answer_dict, self.list_id_questions)

    def check_answer(self) -> list:
        list_answer = self.db.check_answer_applicants(self.applicant_id)
        return list_answer

    def get_answer_list(self) -> tuple:
        list_tuple = self.db.get_answer_list_applicants(self.applicant_id)

        text_answer = [list_tuple[i][1] for i in range(len(list_tuple))]

        id_questions = tuple([list_tuple[i][0] for i in range(len(list_tuple))])
        return text_answer, id_questions
