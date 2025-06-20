#!/usr/bin/env python3
"""
Authentication module
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """Hash a password using bcrypt

    Args:
        password (str): Password to hash

    Returns:
        bytes: Salted and hashed password
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Generate a new UUID

    Returns:
        str: String representation of a new UUID
    """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """Initialize Auth with a DB instance"""
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

    def valid_login(self, email, password: str) -> bool:
        """Validate user credentials

        Args:
            email (str): User's email
            password (str): User's password

        Returns:
            bool: True if credentials are valid, False otherwise
        """
        try:
            user = self._db(email=email)
            return bcrypt.checkpw(password.encode('utf-8'), user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """Create a session for a user

        Args:
            email (str): User's email

        Returns:
            str: Session ID as a string, or None if user not found
        """
        try:
            user = self._db(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None


    def get_user_from_session_id(self, session_id: str) -> User | None:
        """Find user by session ID

        Args:
            session_id (str): Session ID

        Returns:
            User | None: Corresponding User object or None if not found
        """
        if session_id is None:
            return None
        try:
            return self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None
