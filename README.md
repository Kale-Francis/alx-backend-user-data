Personal Data Project
Overview
This project focuses on handling personal data securely in a backend application, with an emphasis on protecting Personally Identifiable Information (PII). It implements logging with PII obfuscation, secure database connections, and password encryption using Python 3.7 on Ubuntu 18.04 LTS. The project adheres to strict security practices, such as obfuscating sensitive data in logs, using environment variables for database credentials, and encrypting passwords.
Learning Objectives
At the end of this project, you should be able to explain:

What constitutes Personally Identifiable Information (PII)
How to implement a log filter to obfuscate PII fields
How to encrypt passwords and validate them
How to securely connect to a database using environment variables

Requirements

Environment: Ubuntu 18.04 LTS
Python Version: Python 3.7
Code Style: Follows pycodestyle (version 2.5)
File Structure:
All files must be executable and start with #!/usr/bin/env python3
All modules, classes, and functions must have documentation
Functions must be type-annotated


Dependencies:
mysql-connector-python (for database connections)
bcrypt (for password encryption)
Standard Python libraries: re, logging, os



Repository Structure

GitHub Repository: alx-backend-user-data
Directory: 0x00-personal_data
Files:
filtered_logger.py: Handles PII obfuscation, logging, and database connections
encrypt_password.py: Implements password hashing and validation
README.md: Project documentation (this file)
user_data.csv: Sample data file containing user information (not included in repo)



Setup Instructions

Clone the Repository:
git clone https://github.com/your-username/alx-backend-user-data.git
cd alx-backend-user-data/0x00-personal_data


Install Dependencies:
pip3 install mysql-connector-python bcrypt


Set Up MySQL Database:

Ensure MySQL is installed and running.
Create a database and user with the provided SQL script:cat main.sql | mysql -uroot -p


Set environment variables for database credentials:export PERSONAL_DATA_DB_USERNAME=root
export PERSONAL_DATA_DB_PASSWORD=root
export PERSONAL_DATA_DB_HOST=localhost
export PERSONAL_DATA_DB_NAME=my_db




Run the Project:

Execute the main script or individual tasks as needed:./filtered_logger.py





Tasks
0. Regex-ing

File: filtered_logger.py
Description: Implements filter_datum function to obfuscate specified fields in log messages using regex.
Function: filter_datum(fields, redaction, message, separator)
Purpose: Replaces sensitive field values with a redaction string (e.g., xxx) using a single regex operation.

1. Log Formatter

File: filtered_logger.py
Description: Implements RedactingFormatter class, a custom logging formatter that filters PII fields.
Class: RedactingFormatter
Purpose: Formats log records to obfuscate specified fields using filter_datum.

2. Create Logger

File: filtered_logger.py
Description: Implements get_logger function to create a logger named "user_data" with PII filtering.
Constant: PII_FIELDS (tuple of 5 PII fields: name, email, phone, ssn, password)
Purpose: Configures a logger that logs up to INFO level, uses RedactingFormatter, and does not propagate messages.

3. Connect to Secure Database

File: filtered_logger.py
Description: Implements get_db function to connect to a MySQL database using environment variables.
Function: get_db()
Purpose: Securely connects to a database using credentials stored in environment variables (PERSONAL_DATA_DB_USERNAME, PERSONAL_DATA_DB_PASSWORD, PERSONAL_DATA_DB_HOST, PERSONAL_DATA_DB_NAME).

4. Read and Filter Data

File: filtered_logger.py
Description: Implements main function to retrieve and display filtered user data from the database.
Function: main()
Purpose: Queries the users table and logs each row with PII fields obfuscated using the logger from Task 2.

5. Encrypting Passwords

File: encrypt_password.py
Description: Implements hash_password function to hash passwords using bcrypt.
Function: hash_password(password)
Purpose: Generates a salted, hashed password as a byte string.

6. Check Valid Password

File: encrypt_password.py
Description: Implements is_valid function to validate passwords against their hashed versions.
Function: is_valid(hashed_password, password)
Purpose: Checks if a provided password matches a hashed password using bcrypt.

Usage Example

Test PII Obfuscation:
./main.py  # Example from Task 0

Output:
name=egg;email=eggmin@eggsample.com;password=xxx;date_of_birth=xxx;
name=bob;email=bob@dylan.com;password=xxx;date_of_birth=xxx;


Test Database Connection and Logging:
PERSONAL_DATA_DB_USERNAME=root PERSONAL_DATA_DB_PASSWORD=root PERSONAL_DATA_DB_HOST=localhost PERSONAL_DATA_DB_NAME=my_db ./filtered_logger.py

Output:
[HOLBERTON] user_data INFO 2019-11-19 18:37:59,596: name=***; email=***; phone=***; ssn=***; password=***; ip=60ed:c396:2ff:244:bbd0:9208:26f2:93ea; last_login=2019-11-14 06:14:24; user_agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36;


Test Password Encryption:
./main.py  # Example from Task 5 & 6

Output:
b'$2b$12$Fnjf6ew.oPZtVksngJjh1.vYCnxRjPm2yt18kw6AuprMRpmhJVxJO'
True



Resources

What Is PII, non-PII, and Personal Data?
Python Logging Documentation
bcrypt Package
Logging to Files, Setting Levels, and Formatting

Notes

Ensure environment variables are set before running the project to avoid database connection errors.
The project must be completed by May 23, 2025, 6:00 AM.
Request a manual QA review upon completion.
An auto-review will be launched at the deadline.

