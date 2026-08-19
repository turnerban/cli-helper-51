import os

# Game default configurations
DEFAULT_PLAYER_NAME = 'Player1'
DEFAULT_GAME_LEVEL = 1
DEFAULT_MAX_PLAYERS = 4

# Error messages
ERROR_MESSAGES = {
    'player_limit_exceeded': 'Maximum number of players exceeded.',
    'invalid_player_name': 'Player name cannot be empty or contain special characters.',
    'invalid_game_level': 'Game level must be between 1 and 100.',
}

# Default settings
DEFAULT_SETTINGS = {
    'max_players': DEFAULT_MAX_PLAYERS,
    'game_level': DEFAULT_GAME_LEVEL,
}

# Validation regex
PLAYER_NAME_REGEX = r'^[a-zA-Z0-9_]+$'

# Function to validate player name
def validate_player_name(name):
    if not name or not re.match(PLAYER_NAME_REGEX, name):
        raise ValueError(ERROR_MESSAGES['invalid_player_name'])

# Function to validate game level
def validate_game_level(level):
    if level < 1 or level > 100:
        raise ValueError(ERROR_MESSAGES['invalid_game_level'])

# Check player limits
def check_player_limit(current_count):
    if current_count > DEFAULT_MAX_PLAYERS:
        raise ValueError(ERROR_MESSAGES['player_limit_exceeded'])
