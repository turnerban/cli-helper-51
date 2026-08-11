import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

def is_strong_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True

def is_positive_integer(value):
    return isinstance(value, int) and value > 0

def is_valid_url(url):
    pattern = r'^(https?://)?(www\.)?([a-zA-Z0-9-]+\.[a-zA-Z]{2,})$'
    return re.match(pattern, url) is not None

def is_not_empty_string(s):
    return isinstance(s, str) and bool(s.strip())