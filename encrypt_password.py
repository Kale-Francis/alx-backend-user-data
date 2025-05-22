#!/usr/bin/env python3
"""
Module for password encryption and validation
"""
import bcrypt

# Task 5: Encrypt passwords
def hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt with automatic salt
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Task 6: Check valid password
def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validate if provided password matches the hashed password
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)