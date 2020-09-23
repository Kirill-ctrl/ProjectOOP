import psycopg2


class DataBase:
    DB_NAME = 'Recruit'
    USER_NAME = 'postgres'
    PASSWORD = 'k197908'

    def __init__(self):
        self.conn, self.cur = self.connecting()

    def connecting(self):
        with psycopg2.connect(f"dbname={self.DB_NAME} user={self.USER_NAME} password='{self.PASSWORD}'") as conn:
            cur = conn.cursor()
        return conn, cur


class ApplicantTable(DataBase):

    def applicant_list(self):
        self.cur.execute(f"SELECT * FROM applicant ORDER BY id")
        list_tuple = self.cur.fetchall()
        return list_tuple

    def update_category_questions(self, code, email):
        self.cur.execute(f"UPDATE applicant SET question_list_code = {code} WHERE email = '{email}'")
        self.conn.commit()

    def applicant_list_for_employers(self):
        self.cur.execute("SELECT applicant_name, city, age, email, question_list_code FROM applicant WHERE accept = false ORDER BY id")
        list_tuples = self.cur.fetchall()
        return list_tuples

    def update_applicant_accepted(self, employer_id, applicant_email):
        self.cur.execute(f"UPDATE applicant SET employer_id = {employer_id}, accept = true WHERE email = '{applicant_email}'")
        self.conn.commit()

    def get_data_by_email(self, email):
        self.cur.execute(f"SELECT applicant.applicant_name, users.email, users.status, applicant.users_id, applicant.id FROM users INNER JOIN applicant ON "
                         f"applicant.users_id = users.id WHERE users.email = '{email}'")
        list_tuple = self.cur.fetchall()
        return list_tuple

    def new_applicant(self, name: str, city: str, age: int, email: str, users_id: int):
        self.cur.execute(f"INSERT INTO applicant(applicant_name, city, age, email, users_id) VALUES ('{name}', '{city}', {age}, '{email}', {int(users_id)})")
        self.conn.commit()


class EmployerTable(DataBase):

    def employer_list(self):
        self.cur.execute("SELECT employer_name, city FROM employer ORDER BY id")
        list_tuple = self.cur.fetchall()
        return list_tuple

    def new_employer(self, name: str, city: str, users_id: int):
        self.cur.execute(f"INSERT INTO employer(employer_name, city, users_id) VALUES ('{name}', '{city}', {int(users_id)})")
        self.conn.commit()

    def get_id_by_email(self, employer_email: str):
        self.cur.execute(f"SELECT employer.id FROM employer INNER JOIN users ON users.id = employer.users_id WHERE email = '{employer_email}'")
        employer_id = self.cur.fetchone()[0]
        return employer_id


class TokenTable(DataBase):

    def insert_token(self, token, user_id, time_now):
        self.cur.execute(f"""INSERT INTO token(token_text, user_id, token_time) VALUES ('{token}', {int(user_id)}, '{time_now}')""")
        self.conn.commit()

    def amount_of_authorizations(self, email):
        self.cur.execute(f"SELECT COUNT(token.id) FROM token INNER JOIN users ON token.user_id = users.id WHERE email = '{email}' AND token_status = true")
        count = self.cur.fetchone()[0]
        return count

    def insert_new_temporary_token(self, new_token_temp, user_id, time_now, new_date, email):
        self.cur.execute(f"""INSERT INTO token(token_text, user_id, token_time, save_temp, token_status) VALUES ('{new_token_temp}', {int(user_id)}, '{time_now}', '{new_date}', {True})""")
        self.conn.commit()
        # cur.execute(f"UPDATE token SET token_status = True, token_time = '{time_now}' WHERE user_id = (SELECT id FROM users WHERE email = '{email}') AND token_status = false")
        # conn.commit()

    def get_status_and_user_id_by_email(self, email):
        self.cur.execute(f"SELECT status, token.id FROM users INNER JOIN token ON token.user_id = users.id WHERE email = '{email}' ORDER BY token.id")
        list_tuples = self.cur.fetchall()
        return list_tuples

    def update_token_status(self, time_now, email):
        self.cur.execute(f"UPDATE token SET token_status = True, token_time = '{time_now}' WHERE user_id = (SELECT id FROM users WHERE email = '{email}') AND token_status = false")
        self.conn.commit()

    def get_single_token(self, email):
        self.cur.execute(f"SELECT token_text FROM token INNER JOIN users ON users.id = token.user_id WHERE email = '{email}'")
        token = self.cur.fetchone()[0]
        return token

    def get_save_time(self, email):
        self.cur.execute(f"SELECT save_temp FROM token INNER JOIN users ON token.user_id = users.id WHERE email = '{email}'")
        save_temp = self.cur.fetchall()
        return save_temp

    def get_bool_value_token_status(self, token):
        self.cur.execute(f"SELECT token_status FROM token WHERE token_text = '{token}'")
        bool_value = self.cur.fetchone()[0]
        return bool_value

    def remove_expired_tokens(self, list_save_temp):
        self.cur.execute(f"DELETE FROM token WHERE save_temp IN {list_save_temp}")
        self.conn.commit()


class AnswerTable(DataBase):

    def insert_answer_applicants(self, applicant_id, key_answer_dict, list_questions_id):
        for i in range(len(list_questions_id)):
            self.cur.execute(f"INSERT INTO answer VALUES ({applicant_id}, '{key_answer_dict[i]}', {list_questions_id[i][0]})")
            self.conn.commit()

    def check_answer_applicants(self, applicant_id):
        self.cur.execute(f"SELECT user_id, id_quest FROM answer WHERE user_id = {applicant_id}")
        list_answer = self.cur.fetchall()
        return list_answer

    def get_answer_list_applicants(self, applicant_id):
        self.cur.execute(f"SELECT id_quest, text_answer FROM answer WHERE user_id = {applicant_id}")
        list_tuple = self.cur.fetchall()
        return list_tuple


class UsersTable(DataBase):

    def adding_new_user(self, name, email, password, status):
        self.cur.execute(f"INSERT INTO users(name, email, psw, status) VALUES ('{name}', '{email}', '{password}', '{status}')")
        self.conn.commit()

    def get_id_new_user(self, email):
        self.cur.execute(f"SELECT id FROM users WHERE email = '{email}'")
        users_id = self.cur.fetchone()[0]
        return users_id

    def get_id_user(self, email):
        self.cur.execute(f"SELECT id FROM users WHERE email = '{email}'")
        user_id = self.cur.fetchone()[0]
        return user_id

    def get_password(self, email):
        self.cur.execute(f"SELECT psw FROM users WHERE email = '{email}'")
        list_tuple = self.cur.fetchone()
        return list_tuple[0]

    def get_status_users(self, email):
        self.cur.execute(f"SELECT status FROM users INNER JOIN token ON token.user_id = users.id WHERE email = '{email}' ORDER BY token.id")
        status = self.cur.fetchone()[0]
        return status

    def get_email_user_by_token(self, token):
        self.cur.execute(f"SELECT email FROM users INNER JOIN token ON users.id = user_id WHERE token_text = '{token}'")
        email = self.cur.fetchone()[0]
        return email

    def log_out(self, token):
        self.cur.execute(f"UPDATE users SET login = False WHERE id = (SELECT user_id FROM token WHERE token_text = '{token}')")
        self.conn.commit()


class QuestionTable(DataBase):

    def get_text_questions(self, random_id):
        self.cur.execute(f"SELECT quest_text FROM question WHERE question_list_id = {random_id} ORDER BY id")
        list_tuples = self.cur.fetchall()
        return list_tuples

    def select_list_question_id(self, code):
        self.cur.execute(f"SELECT question.id  FROM question_list INNER JOIN question ON question_list_id = question_list.id WHERE code = {code}")
        list_id_questions = self.cur.fetchall()
        return list_id_questions

    def get_question_text_by_id_question(self, id_question):
        self.cur.execute(f"SELECT quest_text FROM question WHERE id in {id_question}")
        list_tuple = self.cur.fetchall()
        return list_tuple


class QuestionListTable(DataBase):

    def get_list_id(self):
        self.cur.execute("SELECT id FROM question_list ")
        list_tuples = self.cur.fetchall()
        return list_tuples

    def select_question_code(self, random_id):
        self.cur.execute(f"SELECT code FROM question_list WHERE id = {random_id}")
        list_tuple = self.cur.fetchone()
        return list_tuple
