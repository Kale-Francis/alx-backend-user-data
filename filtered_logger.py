#!/usr/bin/env python3
"""
Module for logging user data with PII obfuscation
"""
import re
import logging
import os
import mysql.connector
from typing import List, Tuple

# Task 2: Define PII fields
PII_FIELDS: Tuple[str, ...] = ("name", "email", "phone", "ssn", "password")

# Task 0: Regex-based PII obfuscation
def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Obfuscate specified fields in a log message using regex
    """
    pattern = f"({'|'.join(fields)})=([^;]*?){separator}"
    return re.sub(pattern, f"\\1={redaction}{separator}", message)

# Task 1: Custom log formatter with PII redaction
class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format log record with PII fields redacted
        """
        record.msg = filter_datum(self.fields, self.REDACTION, record.msg, self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)

# Task 2: Create logger with PII filtering
def get_logger() -> logging.Logger:
    """
    Create and configure a logger for user data with PII filtering
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(fields=PII_FIELDS))
    logger.addHandler(stream_handler)
    
    return logger

# Task 3: Connect to secure database
def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Connect to MySQL database using environment variables
    """
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    database = os.getenv("PERSONAL_DATA_DB_NAME")
    
    return mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=database
    )

# Task 4: Read and filter data
def main():
    """
    Retrieve and display filtered user data from database
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    
    logger = get_logger()
    columns = ["name", "email", "phone", "ssn", "password", "ip", "last_login", "user_agent"]
    
    for row in cursor:
        message = ";".join(f"{col}={val}" for col, val in zip(columns, row))
        logger.info(message)
    
    cursor.close()
    db.close()

if __name__ == "__main__":
    main()