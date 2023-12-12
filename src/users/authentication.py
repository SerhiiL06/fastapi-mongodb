from database.connection import user
from .password import HashedPassword, PasswordIncorrect
from .exceptions import UserAbsent
from fastapi import status


class UserAuth:
    def login_user(self, user_data):
        current_user = self.check_exists_user(user_data.email)

        self.verify_password(user_data.password, current_user.get("password"))

        return True

    @classmethod
    def check_exists_user(cls, email):
        user_exists = user.find_one({"email": email})

        if not user_exists:
            raise UserAbsent(detail="user with this email doesn't exists")
        return user_exists

    @classmethod
    def verify_password(cls, secret, hashed):
        bcrypt = HashedPassword()

        if not bcrypt.verify_password(secret, hashed):
            raise PasswordIncorrect(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Wrong Password"
            )
