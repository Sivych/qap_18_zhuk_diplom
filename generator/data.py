from dataclasses import dataclass


@dataclass
class NewUser:
    first_name: str = None
    last_name: str = None
    email: str = None
    password: str = None
    password_confirm: str = None


class DatasetLogin:
    dataset_email = str('KZhuk111@mail.com')
    dataset_password = str('123456Aabc')