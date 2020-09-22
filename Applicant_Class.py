from connect import connecting


class Applicant:

    def give_information_applicant(self, name: str, email: str, token: str, status: str, users_id: int):
        self.name = name
        self.email = email
        self.token = token
        self.status = status
        self.user_id = users_id

    def give_applicant_id(self, applicant_id: int):
        self.applicant_id = applicant_id

    @staticmethod
    def get_applicant_list() -> list:
        conn, cur = connecting()
        cur.execute(f"SELECT * FROM applicant ORDER BY id")
        list_tuple = cur.fetchall()
        return list_tuple

    def update_cat(self, code: int):
        """Изменяем поле на значение категории вопросов, на которые ответил соискатель"""
        conn, cur = connecting()
        cur.execute(f"UPDATE applicant SET question_list_code = {code} WHERE email = '{self.email}'")
        conn.commit()

    @staticmethod
    def list_for_employers() -> list:
        """Получение данных по соискателям"""
        conn, cur = connecting()
        cur.execute("SELECT applicant_name, city, age, email, question_list_code FROM applicant WHERE accept = false ORDER BY id")
        list_tuples = cur.fetchall()
        return list_tuples

    @staticmethod
    def accept_applicant(employer_id: int, applicant_email: str):
        conn, cur = connecting()
        cur.execute(f"UPDATE applicant SET employer_id = {employer_id}, accept = true WHERE email = '{applicant_email}'")
        conn.commit()

    @staticmethod
    def get_information_from_email(email: str) -> tuple:
        conn, cur = connecting()
        cur.execute(f"SELECT applicant.applicant_name, users.email, users.status, applicant.users_id, applicant.id FROM users INNER JOIN applicant ON "
                    f"applicant.users_id = users.id WHERE users.email = '{email}'")
        s = cur.fetchall()
        name = s[0][0]
        email = s[0][1]
        status = s[0][2]
        users_id = s[0][3]
        applicant_id = s[0][4]
        return name, email, status, users_id, applicant_id

    @staticmethod
    def add_new_applicant(name: str, city: str, age: int, email: str, users_id: int):
        conn, cur = connecting()
        cur.execute(f"INSERT INTO applicant(applicant_name, city, age, email, users_id) VALUES ('{name}', '{city}', {age}, '{email}', {int(users_id)})")
        conn.commit()
