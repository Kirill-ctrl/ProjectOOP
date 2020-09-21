from flask import Flask, request
from applicant_list import get_inf_applicant, get_applicant_list_for_employer
from employer_list import get_inf_employer
from question_all import get_questions
from answer_all import insert_answer_applicant
from answer_list_applicant import get_list_answer_applicant
from accept_on_work import accept_applicant
from register import sign_up
from authentification import auth
from logout import log_out

app = Flask(__name__)


@app.route('/applicant')
def applicant():
    token = request.headers['Token']
    return get_inf_applicant(token)


@app.route('/employer')
def employer():
    token = request.headers['Token']
    return get_inf_employer(token)


@app.route('/quest')
def quest():
    token = request.headers['Token']
    return get_questions(token)


@app.route('/answer', methods=['POST'])
def answer():
    list_answer_applicant = request.json
    code = request.headers['code']
    token = request.headers['Token']
    return insert_answer_applicant(list_answer_applicant, code, token)


@app.route("/list")
def get_list():
    token = request.headers['Token']
    return get_applicant_list_for_employer(token)


@app.route('/answer_list')
def answer_list():
    token = request.headers['Token']
    email = request.headers['Email']
    return get_list_answer_applicant(token, email)


@app.route('/accept')
def accept():
    token = request.headers['Token']
    employer_email = request.headers['Employer-email']
    applicant_email = request.headers['Applicant-email']
    return accept_applicant(token, employer_email, applicant_email)


@app.route('/register', methods=['POST'])
def register():
    data = request.json
    return sign_up(data)


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    return auth(data)


@app.route('/logout')
def logout():
    token = request.headers['Token']
    return log_out(token)


if __name__ == '__main__':
    app.run()
