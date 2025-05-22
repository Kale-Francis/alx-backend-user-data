#!/usr/bin/env python3
"""
Module to obfuscate sensitive fields in log messages using regex.
"""
import re
from typing import List

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Obfuscates specified fields in a log message.

    Args:
        fields: List of strings representing fields to obfuscate.
        redaction: String to replace the field values with.
        message: The log message to process.
        separator: Character separating fields in the message.

    Returns:
        The obfuscated log message.
    """
    pattern = f"({'|'.join(fields)})=.*?{separator}"
    return re.sub(pattern, f"\\1={redaction}{separator}", message)
