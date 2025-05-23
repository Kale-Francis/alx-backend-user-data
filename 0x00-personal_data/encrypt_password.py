#!/usr/bin/env python3
"""
Module to hash passwords securely using bcrypt.
"""
import bcrypt

def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt with a random salt.

    Args:
        password: The password string to hash.

    Returns:
        A salted, hashed password as a byte string.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
