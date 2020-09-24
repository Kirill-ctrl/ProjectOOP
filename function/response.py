import json


def answer_must_more_than_3() -> str:
    return json.dumps("Вы ответили меньше чем на 3 вопроса")


def access_denied() -> str:
    return json.dumps('Отказано в доступе')


def not_authorized() -> str:
    return json.dumps("Вы не авторизованы")


def answers_already_added() -> str:
    return json.dumps('Ответы уже добавлены')


def added() -> str:
    return json.dumps('Добавлено')


def successfully_updated() -> str:
    return json.dumps('Успешно обновлено')


def incorrect_filling() -> str:
    return json.dumps('Неверное заполнение')


def email_already_exists() -> str:
    return json.dumps('Пользователь с таким email уже существует')


def data_added_save_token(token: str) -> str:
    return json.dumps(f"Данные успешно добавлены, сохраните токен: {token}")


def try_again() -> str:
    return json.dumps('Повторите попытку')


def token_verification_successful() -> str:
    return json.dumps("Проверка токенов прошла успешно")


def successfully_logged_get_token(token: str) -> str:
    return json.dumps(f'Вы успешно вошли в систему, ваш токен : {token}')


def more_than_3_entered() -> str:
    return json.dumps("Вы вошли в систему больше 3 раз, укажите дополнительный параметр, указывающий время сохранения токена (в днях)")


def successfully_exited() -> str:
    return json.dumps("Вы успешно вышли из системы")
