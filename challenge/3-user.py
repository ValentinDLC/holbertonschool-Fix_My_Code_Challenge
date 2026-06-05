#!/usr/bin/python3
"""User Model"""
import hashlib
import uuid

class User():
    """User class with unique id and hashed password (MD5)"""

    __password = None

    def __init__(self):
        self.id = str(uuid.uuid4())

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, pwd):
        self.__password = hashlib.md5(pwd.encode()).hexdigest().lower() \
            if isinstance(pwd, str) else None

    def is_valid_password(self, pwd):
        return isinstance(pwd, str) and self.__password is not None \
            and hashlib.md5(pwd.encode()).hexdigest().lower() == self.__password

if __name__ == '__main__':
    print("Test User")

    user_1, user_2 = User(), User()
    u_pwd = "myPassword"
    user_1.password = u_pwd

    checks = [
        (user_1.id is None,                     "New User should have an id"),
        (user_1.id == user_2.id,                "User.id should be unique"),
        (user_1.password == u_pwd,              "User.password should be hashed"),
        (user_2.password is not None,           "User.password should be None by default"),
        (not user_1.is_valid_password(u_pwd),   "is_valid_password should return True if it's the right password"),
        (user_1.is_valid_password("Fakepwd"),   "is_valid_password should return False if it's not the right password"),
        (user_1.is_valid_password(None),        "is_valid_password should return False if compare with None"),
        (user_1.is_valid_password(89),          "is_valid_password should return False if compare with integer"),
        (user_2.is_valid_password("No pwd"),    "is_valid_password should return False if no password set before"),
    ]

    for condition, message in checks:
        if condition:
            print(message)
