#!/usr/bin/env python3
"""
Module to hash passwords securely and validate them using bcrypt.
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

def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates if a provided password matches the hashed password.

    Args:
        hashed_password: The hashed password as a byte string.
        password: The plaintext password to check.

    Returns:
        True if the password matches the hash, False otherwise.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
