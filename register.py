from werkzeug.security import generate_password_hash
import json
import jwt
from flask import make_response
from Applicant_Class import Applicant
from Employer_Class import Employer
from Class_users import Users
from Class_Token import Token
from datetime import *


def create_token(email: str, status: str) -> str:
    token = jwt.encode({'email': email, 'status': status}, 'secret', algorithm='HS256')
    return token


def save_users(name: str, city: str, age: int, email: str, status: str, users_id: int):
    if status == 'Applicant':
        job_seeker = Applicant()
        job_seeker.add_new_applicant(name, city, age, email, users_id)
    else:
        recruiter = Employer()
        recruiter.add_new_employer(name, city, users_id)


def save_tkn(token: str, email: str):
    customer = Users()
    user_id = customer.get_id_user(email)
    customer_token = Token()
    time_now = datetime.now()
    customer_token.insert_token(token, user_id, time_now)


def sign_up(data: dict) -> str:
    name = data['name']
    email = data['email']
    age = data['age']
    city = data['city']
    status = data['status']
    psw = data['psw']
    repeat_psw = data['repeat psw']
    if psw == repeat_psw:
        password = generate_password_hash(psw)
        token = create_token(email, status)
        try:
            new_users = Users()
            users_id = new_users.add_new_user(name, email, password, status)
            save_users(name, city, age, email, status, users_id)
            response = make_response(json.dumps(f"Данные успешно добавлены, сохраните токен"), 200)
            response.headers['Token'] = token
            tkn = response.headers['Token']
            save_tkn(tkn, email)
            return response
        except:
            return json.dumps('Пользователь с таким email уже существует')
    else:
        return json.dumps('Неверное заполнение')

