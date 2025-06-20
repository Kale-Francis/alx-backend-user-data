#!/usr/bin/env python3
"""
Authentication module
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Hash a password using bcrypt

    Args:
        password (str): Password to hash

    Returns:
        bytes: Salted and hashed password
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
