import re

def process_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError('Input must be a string')
    if len(user_input) < 3:
        raise ValueError('Input must be at least 3 characters long')
    if len(user_input) > 20:
        raise ValueError('Input must not exceed 20 characters')
    if not re.match('^[a-zA-Z0-9_]+$', user_input):
        raise ValueError('Input must be alphanumeric and can include underscores')
    return user_input

def main_loop():
    while True:
        user_input = input('Enter your command: ')
        try:
            validated_input = process_input(user_input)
            print(f'Processing: {validated_input}')
            # Further processing code here
        except ValueError as ve:
            print(f'Error: {ve}')

if __name__ == '__main__':
    main_loop()