from connect import connecting


def get_status(token: str) -> str:
    conn, cur = connecting()
    cur.execute(f"SELECT status FROM token INNER JOIN users ON users.id = token.user_id WHERE token_text = '{token}'")
    status = cur.fetchone()
    status = status[0]
    return status
