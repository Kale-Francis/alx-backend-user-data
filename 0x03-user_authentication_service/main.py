#!/usr/bin/env python3
"""
Main module for end-to-end integration tests
"""
import requests


def register_user(email: str, password: str) -> None:
    """Test POST /users to register a user

    Args:
        email (str): User's email
        password (str): User's password
    """
    url = 'http://localhost:5000/users'
    data = {'email': email, 'password': password}
    response = requests.post(url, data=data)
    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "user created"}


def log_in_wrong_password(email: str, password: str) -> None:
    """Test POST /sessions with incorrect password

    Args:
        email (str): User's email
        password (str): Incorrect password
    """
    url = 'http://localhost:5000/sessions'
    data = {'email': email, 'password': password}
    response = requests.post(url, data=data)
    assert response.status_code == 401


def log_in(email: str, password: str) -> str:
    """Test POST /sessions to log in a user

    Args:
        email (str): User's email
        password (str): User's password

    Returns:
        str: Session ID from cookies
    """
    url = 'http://localhost:5000/sessions'
    data = {'email': email, 'password': password}
    response = requests.post(url, data=data)
    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "logged in"}
    return response.cookies.get('session_id')


def profile_unlogged() -> None:
    """Test GET /profile without session cookie"""
    url = 'http://localhost:5000/profile'
    response = requests.get(url)
    assert response.status_code == 403


def profile_logged(session_id: str) -> None:
    """Test GET /profile with valid session cookie

    Args:
        session_id (str): Session ID cookie
    """
    url = 'http://localhost:5000/profile'
    cookies = {'session_id': session_id}
    response = requests.get(url, cookies=cookies)
    assert response.status_code == 200
    assert "email" in response.json()


def log_out(session_id: str) -> None:
    """Test DELETE /sessions to log out a user

    Args:
        session_id (str): Session ID cookie
    """
    url = 'http://localhost:5000/sessions'
    cookies = {'session_id': session_id}
    response = requests.delete(url, cookies=cookies)
    assert response.status_code == 302


def reset_password_token(email: str) -> str:
    """Test POST /reset_password to get reset token

    Args:
        email (str): User's email

    Returns:
        str: Reset password token
    """
    url = 'http://localhost:5000/reset_password'
    data = {'email': email}
    response = requests.post(url, data=data)
    assert response.status_code == 200
    payload = response.json()
    assert "email" in payload and "reset_token" in payload
    assert payload["email"] == email
    return payload["reset_token"]


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Test PUT /reset_password to update password

    Args:
        email (str): User's email
        reset_token (str): Reset password token
        new_password (str): New password
    """
    url = 'http://localhost:5000/reset_password'
    data = {'email': email, 'reset_token': reset_token,
            'new_password': new_password}
    response = requests.put(url, data=data)
    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "Password updated"}


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
