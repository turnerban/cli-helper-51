import json
from typing import Any, Dict, List, Union

def load_game_data(file_path: str) -> Union[Dict[str, Any], None]:
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f'Error loading game data: {e}')
        return None

def save_game_data(file_path: str, data: Dict[str, Any]) -> bool:
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
            return True
    except IOError as e:
        print(f'Error saving game data: {e}')
        return False

def update_player_score(data: Dict[str, Any], player_id: str, score: int) -> Dict[str, Any]:
    if player_id in data['players']:
        data['players'][player_id]['score'] += score
    else:
        data['players'][player_id] = {'score': score}
    return data

def get_top_players(data: Dict[str, Any], count: int = 5) -> List[Dict[str, Any]]:
    return sorted(data['players'].items(), key=lambda x: x[1]['score'], reverse=True)[:count]