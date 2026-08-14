import random
import json

def generate_random_username(length=8):
    letters = 'abcdefghijklmnopqrstuvwxyz0123456789'
    username = ''.join(random.choice(letters) for _ in range(length))
    return username

def save_high_score(player_name, score, file_path='high_scores.json'):
    try:
        high_scores = load_high_scores(file_path)
    except FileNotFoundError:
        high_scores = {}
    high_scores[player_name] = max(high_scores.get(player_name, 0), score)
    with open(file_path, 'w') as f:
        json.dump(high_scores, f)

def load_high_scores(file_path='high_scores.json'):
    with open(file_path, 'r') as f:
        return json.load(f)

def get_top_scores(file_path='high_scores.json', top_n=5):
    high_scores = load_high_scores(file_path)
    return dict(sorted(high_scores.items(), key=lambda item: item[1], reverse=True)[:top_n])

if __name__ == '__main__':
    print(generate_random_username())
    save_high_score('player1', 150)
    print(get_top_scores())