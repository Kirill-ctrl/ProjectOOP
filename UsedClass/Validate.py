from marshmallow import Schema, fields, post_load, validate


class ValidateRegistration(Schema):
    """Валидируем регистрацию"""
    name = fields.String(required=True, error_messages={"required": "name is required"})
    email = fields.Email(required=True, error_messages={"required": "email is required", "invalid": "invalid email"})
    age = fields.Integer(required=True, error_messages={"required": "age is required"})
    city = fields.String(required=True, error_messages={"required": "city is required"})
    psw = fields.String(required=True, error_messages={"required": "psw is required"})
    repeat_psw = fields.String(required=True, error_messages={"required": "repeat_psw is required"})
    status = fields.String(required=True, error_messages={"required": "status is required"}, validate=validate.OneOf(["Applicant", "Employer"]))


class ValidateAuthorization(Schema):
    """Валидируем авторизацию"""
    email = fields.Email(required=True, error_messages={"required": "email is required", "invalid": "invalid email"})
    psw = fields.String(required=True, error_messages={"required": "psw is required"})


class ValidateAnswerApplicant(Schema):
    """Валидируем ответы пользователя"""
    PythonInterpreter = fields.String(partial=True)
    FlaskOrDjango = fields.String(partial=True)
    HashTable = fields.String(partial=True)
    Async = fields.String(partial=True)
    PythonTesting = fields.String(partial=True)
    PythonDebugging = fields.String(partial=True)
    HTML = fields.String(partial=True)
    CSS = fields.String(partial=True)
    JS = fields.String(partial=True)
    FrameworkJS = fields.String(partial=True)
    HTTP_Protocol = fields.String(partial=True)
    FTP_Protocol = fields.String(partial=True)
    Postman = fields.String(partial=True)
    Ajax = fields.String(partial=True)
    SPA = fields.String(partial=True)
    GIT = fields.String(partial=True)
    Traceable_and_non_tracing = fields.String(partial=True)
    Conflicts = fields.String(partial=True)
    CopyProject = fields.String(partial=True)

