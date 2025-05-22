#!/usr/bin/env python3
"""
Module to obfuscate sensitive fields in log messages using regex and format logs.
"""
import re
from typing import List
import logging

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

class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize the formatter with fields to redact.

        Args:
            fields: List of strings representing fields to obfuscate in log messages.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record, obfuscating specified fields.

        Args:
            record: The log record to format.

        Returns:
            The formatted and obfuscated log message.
        """
        record.msg = filter_datum(self.fields, self.REDACTION, record.msg, self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)
