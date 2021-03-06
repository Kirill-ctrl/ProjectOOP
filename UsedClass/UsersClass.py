from DBClass.DataBaseClass import UsersTable


class Users:
    def __init__(self):
        self.db = UsersTable()
        self.name = None
        self.email = None
        self.password = None
        self.status = None
        self.status = None

    def add_new_user(self, name: str, email: str, password: str, status: str) -> None:
        """Получаем информацию по пользователю"""
        self.name = name
        self.email = email
        self.password = password
        self.status = status
        self.db.adding_new_user(name, email, password, status)

    def get_id_user(self) -> int:
        """Получаем id нового пользователя"""
        users_id = self.db.get_id_new_user(self.email)
        return users_id

    def get_id_users(self, email: str) -> int:
        """Получаем id пользователя"""
        user_id = self.db.get_id_user(email)
        return user_id

    def get_psw(self, email: str) -> str:
        """Получаем пароль пользователя по email"""
        password = self.db.get_password(email)
        return password

    def get_status(self, email: str) -> str:
        """Получаем статус пользователя по email"""
        status = self.db.get_status_users(email)
        return status

    def get_email(self, token: str) -> str:
        """Получаем email пользователя по token"""
        email = self.db.get_email_user_by_token(token)
        return email

    def exit(self, token: str) -> None:
        """Выходим из системы"""
        self.db.log_out(token)
