import json
from UsedClass.UsersClass import Users
from function.Authentication import get_authorization


def log_out(token: str) -> str:
    if get_authorization(token):
        user = Users()
        user.exit(token)
        return json.dumps("Вы успешно вышли из системы")
    else:
        return json.dumps("Вы не авторизованы")
