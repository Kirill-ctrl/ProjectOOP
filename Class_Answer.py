from connect import connecting
import json


class Answer1:
    def give_data_answer(self, code: int, key_answer_dict: list, quest_id: int):
        self.code = code
        self.quest_id = quest_id
        self.key_answer_dict = key_answer_dict

    def give_applicant_id(self, applicant_id: int):
        self.applicant_id = applicant_id

    def update_answer(self, list_quest_id: list) -> str:
        """Добавляем ответы в таблицу answer"""
        conn, cur = connecting()
        for i in range(len(list_quest_id)):
            cur.execute(f"INSERT INTO answer VALUES ({self.applicant_id}, '{self.key_answer_dict[i]}', {list_quest_id[i][0]})")
            conn.commit()
        return json.dumps('Добавлено')

    def check_answer(self) -> list:
        conn, cur = connecting()
        cur.execute(f"SELECT user_id, id_quest FROM answer WHERE user_id = {self.applicant_id}")
        list_answer = cur.fetchall()
        return list_answer

    def get_answer_list(self) -> tuple:
        conn, cur = connecting()
        cur.execute(f"SELECT id_quest, text_answer FROM answer WHERE user_id = {self.applicant_id}")
        list_tuple = cur.fetchall()

        text_answer = [list_tuple[i][1] for i in range(len(list_tuple))]

        id_question = tuple([list_tuple[i][0] for i in range(len(list_tuple))])
        return text_answer, id_question
