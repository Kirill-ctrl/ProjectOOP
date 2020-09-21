from random import choices
from connect import connecting


class Question:
    def give_random_id(self, random_id: int):
        self.random_id = random_id

    @staticmethod
    def rand() -> int:
        """Выбор случайного id категории вопросов"""
        conn, cur = connecting()
        cur.execute("SELECT id FROM question_list ")
        list_tuples = cur.fetchall()
        list_random = []
        for i in range(len(list_tuples)):
            list_random.append(list_tuples[i][0])
        list_random = choices(list_random, k=1)
        return list_random[0]

    def choice_quest(self) -> list:
        """выбрать вопросы по определенному id"""
        conn, cur = connecting()
        cur.execute(f"SELECT quest_text FROM question WHERE question_list_id = {self.random_id} ORDER BY id")
        list_tuples = cur.fetchall()
        return list_tuples

    def choice_code(self) -> int:
        """Выбрать код этих вопросов"""
        conn, cur = connecting()
        cur.execute(f"SELECT code FROM question_list WHERE id = {self.random_id}")
        list_tuple = cur.fetchone()
        return list_tuple[0]

    def id_quest(self, code: int) -> list:
        conn, cur = connecting()
        cur.execute(f"SELECT id FROM question_list WHERE code = {code}")
        quest_id = (cur.fetchone())[0]
        cur.execute(f"SELECT id FROM question WHERE question_list_id = {quest_id}")
        list_quest_id = cur.fetchall()
        return list_quest_id

    def get_quest_text(self, id_question: int) -> list:
        conn, cur = connecting()
        cur.execute(f"SELECT quest_text FROM question WHERE id in {id_question}")
        b = cur.fetchall()
        text_question = [b[i][0] for i in range(len(b))]
        return text_question
