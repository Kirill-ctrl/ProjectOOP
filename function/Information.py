from UsedClass.UsersClass import Users


def get_status(token: str) -> str:
    user = Users()
    email = user.get_email(token)
    status = user.get_status(email)
    return status
