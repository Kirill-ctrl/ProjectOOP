from connect import connecting


class Users:

    def add_new_user(self, name: str, email: str, password: str, status: str) -> int:
        conn, cur = connecting()
        cur.execute(f"INSERT INTO users(name, email, psw, status) VALUES ('{name}', '{email}', '{password}', '{status}')")
        conn.commit()
        cur.execute(f"SELECT id FROM users WHERE email = '{email}'")
        return cur.fetchone()[0]

    def get_id_user(self, email: str) -> id:
        conn, cur = connecting()
        cur.execute(f"SELECT id FROM users WHERE email = '{email}'")
        user_id = cur.fetchone()[0]
        return user_id

    def get_psw(self, email: str) -> str:
        conn, cur = connecting()
        cur.execute(f"SELECT psw FROM users WHERE email = '{email}'")
        list_tuple = cur.fetchone()
        return list_tuple[0]

    def get_status(self, email: str) -> str:
        conn, cur = connecting()
        cur.execute(f"SELECT status FROM users INNER JOIN token ON token.user_id = users.id WHERE email = '{email}' ORDER BY token.id")
        list_tuple = cur.fetchall()
        status = list_tuple[0][0]
        return status

    def exit(self, token: str):
        conn, cur = connecting()
        cur.execute(f"UPDATE users SET login = False WHERE id = (SELECT user_id FROM token WHERE token_text = '{token}')")
        conn.commit()
