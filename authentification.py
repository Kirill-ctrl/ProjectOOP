from werkzeug.security import check_password_hash
from connect import connecting
import json
import jwt
from flask import make_response, request
from register import save_tkn
from datetime import *
from Class_users import Users
from Class_Token import Token


def auth(data: dict) -> str:
    email = data['email']
    psw = data['psw']
    check_save_token_temp(email)
    user = Users()
    passw = user.get_psw(email)
    password = check_password_hash(passw, psw)
    if password:
        token_users = Token()
        count = token_users.count_authorization(email)
        if count >= 3:
            return get_token_temp(count, email)
        elif count == 0:
            return sign_token(email)
        else:
            return get_new_token(email)
    else:
        return json.dumps('Повторите попытку')


def check_save_token_temp(email: str) -> str:
    conn, cur = connecting()
    token_user = Token()
    save_temp = token_user.get_save_temp(email)
    for i in range(len(save_temp)):
        if save_temp[i][0]:
            d = date.today()
            if save_temp[i][0] - d < timedelta(days=0):
                cur.execute(f"DELETE FROM token WHERE save_temp = '{save_temp[i][0]}'")
                conn.commit()
                return json.dumps("Токен был удален")
    return json.dumps('Проверка токенов была успешно выполнена')


def get_token_temp(count: int, email: str) -> str:
    try:
        user = Users()
        status = user.get_status(email)
        token_time = request.headers['Token-time']
        time_now = datetime.now()
        time_temp = timedelta(days=int(token_time))
        new_date = time_now + time_temp
        r = new_date.isoformat(timespec='hours')
        new_date = r[0:10]
        new_token_temp = jwt.encode({'email': email, 'token_time': token_time, 'i': count + 1, 'status': status}, 'secret', algorithm='HS256')
        response = make_response(json.dumps(f"Данные успешно добавлены, сохраните токен"), 200)
        response.headers['Token'] = new_token_temp
        new_token_temp = response.headers['Token']
        del response.headers['Token']
        user_id = user.get_id_user(email)
        new_token = Token()
        new_token.insert_new_token_temp(new_token_temp, user_id, time_now, new_date, email)
        return json.dumps(f'Вы успешно вошли в систему, ваш токен : {new_token_temp}')
    except:
        return "Вы вошли в систему больше 3 раз, укажите дополнительный параметр, указывающий время сохранения токена (дни)"


def get_new_token(email: str) -> str:
    new_token = Token()
    id, status = new_token.get_status_and_id(email)
    new_token = jwt.encode({'email': email, 'status': status, 'id': id}, 'secret', algorithm='HS256')
    response = make_response(json.dumps(f"Данные успешно добавлены, сохраните токен"), 200)
    response.headers['Token'] = new_token
    new_token = response.headers['Token']
    del response.headers['Token']
    save_tkn(new_token, email)
    time_now = datetime.now()
    new_token.update_status_token(time_now, email)
    return json.dumps(f'Вы успешно вошли в систему, ваш токен : {new_token}')


def sign_token(email: str) -> str:
    new_token = Token()
    token = new_token.sign_token(email)
    time_now = datetime.now()
    new_token.update_status_token(time_now, email)
    return json.dumps(f"Вы успешно вошли в систему, ваш токен: {token}")


def get_authorization(token: str) -> bool:
    token_user = Token()
    bool_value = token_user.get_bool_token_status(token)
    return bool_value
