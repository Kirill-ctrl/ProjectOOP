from connect import connecting
import json
from Class_users import Users
from authentification import get_authorization


def log_out(token: str) -> str:
    if get_authorization(token):
        user = Users()
        user.exit(token)
        return json.dumps("Вы успешно вышли из системы")
    else:
        return json.dumps("Вы не авторизованы")