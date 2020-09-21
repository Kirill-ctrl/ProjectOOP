from connect import connecting


class Token:

    def insert_token(self, token: str, user_id: int, time_now):
        conn, cur = connecting()
        cur.execute(f"""INSERT INTO token(token_text, user_id, token_time) VALUES ('{token}', {int(user_id)}, '{time_now}')""")
        conn.commit()

    def count_authorization(self, email: str) -> int:
        conn, cur = connecting()
        cur.execute(f"SELECT COUNT(token.id) FROM token INNER JOIN users ON token.user_id = users.id WHERE email = '{email}' AND token_status = true")
        count = cur.fetchone()[0]
        return count

    def insert_new_token_temp(self, new_token_temp: str, user_id: int, time_now, new_date, email: str):
        conn, cur = connecting()
        cur.execute(f"""INSERT INTO token(token_text, user_id, token_time, save_temp) VALUES ('{new_token_temp}', {int(user_id)}, '{time_now}', '{new_date}')""")
        conn.commit()
        cur.execute(f"UPDATE token SET token_status = True, token_time = '{time_now}' WHERE user_id = (SELECT id FROM users WHERE email = '{email}') AND token_status = false")
        conn.commit()

    def get_status_and_id(self, email: str) -> tuple:
        conn, cur = connecting()
        cur.execute(f"SELECT status, token.id FROM users INNER JOIN token ON token.user_id = users.id WHERE email = '{email}' ORDER BY token.id")
        y = cur.fetchall()
        id = 0
        for i in range(len(y)):
            id = y[i][1] + 1
        status = y[0][0]
        return id, status

    def update_status_token(self, time_now, email: str):
        conn, cur = connecting()
        cur.execute(f"UPDATE token SET token_status = True, token_time = '{time_now}' WHERE user_id = (SELECT id FROM users WHERE email = '{email}') AND token_status = false")
        conn.commit()

    def sign_token(self, email: str) -> str:
        conn, cur = connecting()
        cur.execute(f"SELECT token_text FROM token INNER JOIN users ON users.id = token.user_id WHERE email = '{email}'")
        token = cur.fetchone()[0]
        return token
