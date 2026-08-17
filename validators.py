import re

def is_valid_username(username):
    return bool(re.match(r'^[a-zA-Z0-9]{3,16}$', username))


def is_valid_email(email):
    return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email))


def is_valid_password(password):
    return (len(password) >= 8 and
            any(char.isdigit() for char in password) and
            any(char.islower() for char in password) and
            any(char.isupper() for char in password) and
            any(char in '!@#$%^&*()' for char in password))


def is_valid_game_id(game_id):
    return isinstance(game_id, int) and game_id > 0


def validate_registration(username, email, password, game_id):
    return (is_valid_username(username) and
            is_valid_email(email) and
            is_valid_password(password) and
            is_valid_game_id(game_id))
