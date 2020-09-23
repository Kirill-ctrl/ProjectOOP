from werkzeug.security import check_password_hash
import json
import jwt
from flask import make_response, request
from function.Registration import save_tkn
from datetime import *
from UsedClass.UsersClass import Users
from UsedClass.TokenClass import Token


def auth(data: dict) -> str:
    email = data['email']
    psw = data['psw']
    check_save_token_temp(email)
    user = Users()
    passw = user.get_psw(email)
    password = check_password_hash(passw, psw)
    if password:
        token_users = Token(email)
        count = token_users.count_authorization()
        if count >= 3:
            return get_token_temp(count, email)
        elif count == 0:
            return first_token_authorization(email)
        else:
            return get_new_token(email)
    else:
        return json.dumps('Повторите попытку')


def check_save_token_temp(email: str) -> str:
    token_user = Token(email)
    save_temp = token_user.get_save_temp()
    list_save_temp = []
    for i in range(len(save_temp)):
        if save_temp[i][0]:
            d = date.today()
            if save_temp[i][0] - d < timedelta(days=0):
                list_save_temp.append(save_temp[i][0])
    token_user.delete_token(list_save_temp)
    return "Проверка токенов прошла успешно"


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
        user_id = user.get_id_users(email)
        new_token = Token(email)
        new_token.insert_new_token_temp(new_token_temp, user_id, time_now, new_date)
        return json.dumps(f'Вы успешно вошли в систему, ваш токен : {new_token_temp}')
    except:
        return "Вы вошли в систему больше 3 раз, укажите дополнительный параметр, указывающий время сохранения токена (дни)"


def get_new_token(email: str) -> str:
    new_token = Token(email)
    user_id, status = new_token.get_status_and_id()
    new_token = jwt.encode({'email': email, 'status': status, 'id': user_id}, 'secret', algorithm='HS256')
    response = make_response(json.dumps(f"Данные успешно добавлены, сохраните токен"), 200)
    response.headers['Token'] = new_token
    new_token = response.headers['Token']
    del response.headers['Token']
    save_tkn(new_token)
    time_now = datetime.now()
    new_token.update_status_token(time_now)
    return json.dumps(f'Вы успешно вошли в систему, ваш токен : {new_token}')


def first_token_authorization(email: str) -> str:
    new_token = Token(email)
    token = new_token.single_token()
    time_now = datetime.now()
    new_token.update_status_token(time_now)
    return json.dumps(f"Вы успешно вошли в систему, ваш токен: {token}")


def get_authorization(token: str) -> bool:
    user = Users()
    email = user.get_email(token)
    token_user = Token(email)
    bool_value = token_user.get_bool_token_status(token)
    return bool_value
