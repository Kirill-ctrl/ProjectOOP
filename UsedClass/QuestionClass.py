from random import choices
from DBClass.DataBaseClass import QuestionTable, QuestionListTable


class Question:

    def __init__(self):
        self.db = QuestionTable()
        self.random_id = None

    def give_random_id(self, random_id: int):
        self.random_id = random_id

    def choice_quest(self) -> list:
        """выбрать вопросы по определенному id"""
        list_tuples = self.db.get_text_questions(self.random_id)
        return list_tuples

    def id_quest(self, code: int) -> list:
        list_id_questions = self.db.select_list_question_id(code)
        return list_id_questions

    def get_quest_text(self, id_questions: list) -> list:
        list_tuple = self.db.get_question_text_by_id_question(id_questions)
        text_question = [list_tuple[i] for i in range(len(list_tuple))]
        return text_question

    def get_id_and_pseudonym(self, key_answer_pseudonym: list) -> list:
        list_tuple = self.db.get_question_id_and_question_pseudonym(key_answer_pseudonym)
        return list_tuple


class QuestionList:

    def __init__(self):
        self.db = QuestionListTable()
        self.random_id = None
        self.code = None

    def rand(self) -> int:
        """Выбор случайного id категории вопросов"""
        list_tuples = self.db.get_list_id()
        list_random = []
        for i in range(len(list_tuples)):
            list_random.append(list_tuples[i][0])
        list_random = choices(list_random, k=1)
        self.random_id = list_random[0]
        return list_random[0]

    def choice_code(self, random_id: int) -> int:
        """Выбрать код вопросов по random_id"""
        list_tuple = self.db.select_question_code(random_id)
        self.code = list_tuple[0]
        return list_tuple[0]
