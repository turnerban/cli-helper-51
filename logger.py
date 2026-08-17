import logging

class GameLogger:
    def __init__(self, name='GameLogger', level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_event(self, event, level=logging.INFO):
        if level == logging.INFO:
            self.logger.info(event)
        elif level == logging.WARNING:
            self.logger.warning(event)
        elif level == logging.ERROR:
            self.logger.error(event)
        else:
            self.logger.debug(event)

    def log_score(self, player, score):
        self.logger.info(f'Player: {player}, Score: {score}') 

    def log_action(self, player, action):
        self.logger.info(f'Player: {player} performed action: {action}')