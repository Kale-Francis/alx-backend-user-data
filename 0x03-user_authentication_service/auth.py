#!/usr/bin/env python3
"""
Authentication module
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """Hash a password using bcrypt

    Args:
        password (str): Password to hash

    Returns:
        bytes: Salted and hashed password
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user

        Args:
            email (str): User's email
            password (str): User's password

        Returns:
            User: The created User object

        Raises:
            ValueError: If a user with the email already exists
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            return self._db.add_user(email, hashed_password)
