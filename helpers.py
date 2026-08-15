import random
import string


def generate_random_username(length=8):
    return 'User_' + ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def save_game_data(game_state):
    with open('save_data.json', 'w') as f:
        json.dump(game_state, f)


def load_game_data():
    with open('save_data.json', 'r') as f:
        return json.load(f)


def calculate_high_score(scores):
    return max(scores) if scores else 0


def format_special_characters(text):
    return ''.join(c if c.isalnum() else '_' for c in text)


if __name__ == '__main__':
    print(generate_random_username())
    game_state = {'level': 5, 'score': 1500}
    save_game_data(game_state)
    print(load_game_data())
    print(calculate_high_score([100, 200, 300]))
    print(format_special_characters('Player @#1!'))