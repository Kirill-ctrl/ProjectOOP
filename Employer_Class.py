from connect import connecting


class Employer:
    def get_information_employer(self, name: str, email: str, token: str, status: str, user_id: int):
        self.name = name
        self.email = email
        self.token = token
        self.status = status
        self.user_id = user_id

    def get_employer_list(self) -> list:
        conn, cur = connecting()
        cur.execute("SELECT employer_name, city FROM employer ORDER BY id")
        list_tuple = cur.fetchall()
        return list_tuple

    def add_new_employer(self, name: str, city: str, users_id: int):
        conn, cur = connecting()
        cur.execute(f"INSERT INTO employer(employer_name, city, users_id) VALUES ('{name}', '{city}', {int(users_id)})")
        conn.commit()

    def get_employer_id(self, employer_email: str) -> int:
        conn, cur = connecting()
        cur.execute(f"SELECT employer.id FROM employer INNER JOIN users ON users.id = employer.users_id WHERE email = '{employer_email}'")
        employer_id = cur.fetchone()[0]
        return employer_id