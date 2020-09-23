from DBClass.DataBaseClass import UsersTable


class Users:
    def __init__(self):
        self.db = UsersTable()
        self.name = None
        self.email = None
        self.password = None
        self.status = None
        self.status = None

    def add_new_user(self, name: str, email: str, password: str, status: str):
        self.name = name
        self.email = email
        self.password = password
        self.status = status
        self.db.adding_new_user(name, email, password, status)

    def get_id_user(self):
        users_id = self.db.get_id_new_user(self.email)
        return users_id

    def get_id_users(self, email: str) -> id:
        user_id = self.db.get_id_user(email)
        return user_id

    def get_psw(self, email: str) -> str:
        password = self.db.get_password(email)
        return password

    def get_status(self, email: str) -> str:
        status = self.db.get_status_users(email)
        return status

    def get_email(self, token):
        email = self.db.get_email_user_by_token(token)
        return email

    def exit(self, token: str):
        self.db.log_out(token)
