0x03. User Authentication Service
Project Overview
This project, part of the ALX Backend curriculum, focuses on building a user authentication service using Python, Flask, SQLAlchemy (version 1.3.x), and bcrypt. The goal is to implement a secure authentication system from scratch, including user registration, login, session management, password reset, and profile access. The project emphasizes understanding core authentication concepts such as API routing, cookie handling, password hashing, and database interactions without relying on external authentication frameworks (e.g., Flask-User).
The service uses a SQLite database to store user data, with SQLAlchemy for ORM-based database interactions. The Flask app exposes RESTful API endpoints to handle user-related operations, and bcrypt is used for secure password hashing. The project also includes an end-to-end integration test to validate the API functionality.
Learning Objectives
At the end of this project, you should be able to explain:

How to declare API routes in a Flask app.
How to get and set cookies in Flask.
How to retrieve form data from requests.
How to return various HTTP status codes.
How to implement secure password hashing with bcrypt.
How to manage database operations with SQLAlchemy.
How to structure an authentication service with separation of concerns.

Requirements

Environment: Ubuntu 18.04 LTS using Python 3 (version 3.7).
Editors: vi, vim, or emacs.
Dependencies: SQLAlchemy 1.3.x, bcrypt (install with pip3 install bcrypt).
File Format:
All files must end with a newline.
Python files must start with #!/usr/bin/env python3.
Code must follow pycodestyle (version 2.5).
All modules, classes, and functions must have documentation.
Documentation must be meaningful sentences, not single words.
All functions must be type-annotated.
All files must be executable.


Constraints:
No external authentication modules (e.g., Flask-User) are allowed.
The Flask app must interact with the database only through the Auth class, not directly with the DB class.
Only public methods of Auth and DB classes should be used outside their respective classes.


File Length: File lengths will be tested using wc.

Repository Structure

GitHub Repository: alx-backend-user-data
Directory: 0x03-user_authentication_service
Files:
README.md: This file, providing an overview of the project.
user.py: Defines the SQLAlchemy User model for the users table.
db.py: Implements the DB class for database operations (add, find, update users).
auth.py: Implements the Auth class for authentication logic (password hashing, user registration, session management, password reset).
app.py: Implements the Flask app with API endpoints for user registration, login, logout, profile access, and password reset.
main.py: Contains end-to-end integration tests for the API endpoints.



Tasks
0. User Model

File: user.py
Defines a SQLAlchemy User model with attributes: id (integer, primary key), email (non-nullable string), hashed_password (non-nullable string), session_id (nullable string), and reset_token (nullable string).

1. Create User

File: db.py
Implements the DB.add_user method to add a user to the database with email and hashed_password, returning the User object.

2. Find User

File: db.py
Implements the DB.find_user_by method to find a user by arbitrary keyword arguments, raising NoResultFound or InvalidRequestError as needed.

3. Update User

File: db.py
Implements the DB.update_user method to update user attributes by user_id, raising ValueError for invalid attributes.

4. Hash Password

File: auth.py
Implements the _hash_password method to hash a password using bcrypt, returning bytes.

5. Register User

File: auth.py
Implements the Auth.register_user method to register a user, checking for existing emails and hashing passwords.

6. Basic Flask App

File: app.py
Sets up a Flask app with a single GET / route returning {"message": "Bienvenue"}.

7. Register User Endpoint

File: app.py
Implements the POST /users route to register a user, returning appropriate JSON responses and status codes.

8. Credentials Validation

File: auth.py
Implements the Auth.valid_login method to validate user credentials using bcrypt.

9. Generate UUIDs

File: auth.py
Implements the _generate_uuid method to generate a UUID string.

10. Get Session ID

File: auth.py
Implements the Auth.create_session method to create and store a session ID for a user.

11. Log In

File: app.py
Implements the POST /sessions route to log in a user, setting a session ID cookie and returning a JSON response.

12. Find User by Session ID

File: auth.py
Implements the Auth.get_user_from_session_id method to retrieve a user by session ID.

13. Destroy Session

File: auth.py
Implements the Auth.destroy_session method to clear a user’s session ID.

14. Log Out

File: app.py
Implements the DELETE /sessions route to log out a user by destroying their session and redirecting to GET /.

15. User Profile

File: app.py
Implements the GET /profile route to return the user’s email based on their session ID.

16. Generate Reset Password Token

File: auth.py
Implements the Auth.get_reset_password_token method to generate and store a reset token for a user.

17. Get Reset Password Token Endpoint

File: app.py
Implements the POST /reset_password route to generate a reset token for a registered user.

18. Update Password

File: auth.py
Implements the Auth.update_password method to update a user’s password using a reset token.

19. Update Password Endpoint

File: app.py
Implements the PUT /reset_password route to update a user’s password with a valid reset token.

20. End-to-End Integration Test

File: main.py
Implements test functions to validate all API endpoints using the requests module, ensuring correct status codes and payloads.

Setup Instructions

Install Dependencies:
pip3 install bcrypt
pip3 install flask
pip3 install sqlalchemy==1.3.24


Create Files:

Save each file (user.py, db.py, auth.py, app.py, main.py) in the 0x03-user_authentication_service directory.
Make each file executable:chmod +x user.py db.py auth.py app.py main.py




Run the Flask App (for testing):
python3 app.py

The app will run on http://0.0.0.0:5000.

Run Integration Tests:In a separate terminal, with the Flask app running:
python3 main.py

No output indicates successful tests.

Push to GitHub:

Create the repository alx-backend-user-data if it doesn’t exist.
Create the directory 0x03-user_authentication_service.
Add each file individually and push to GitHub:git add README.md
git commit -m "Add README.md for user authentication service"
git push

Repeat for each file (user.py, db.py, auth.py, app.py, main.py).



Usage

Start the Flask App:
python3 app.py


Test Endpoints (using curl or a tool like Postman):

Register a user:curl -XPOST localhost:5000/users -d 'email=bob@me.com' -d 'password=mySuperPwd'


Log in:curl -XPOST localhost:5000/sessions -d 'email=bob@me.com' -d 'password=mySuperPwd'


Get profile:curl -XGET localhost:5000/profile -b "session_id=<session_id>"


Log out:curl -XDELETE localhost:5000/sessions -b "session_id=<session_id>"


Request password reset token:curl -XPOST localhost:5000/reset_password -d 'email=bob@me.com'


Update password:curl -XPUT localhost:5000/reset_password -d 'email=bob@me.com' -d 'reset_token=<token>' -d 'new_password=newPwd'




Run Integration Tests:
python3 main.py



Author
[Kale Franis]
License
This project is part of the ALX Backend curriculum and is provided for educational purposes.
