import time
import random

class GameEngine:
    def __init__(self):
        self.score = 0
        self.level = 1
        self.is_running = True

    def run(self):
        while self.is_running:
            self.play()
            if self.score >= 100:
                self.level_up()

    def play(self):
        # Simulate some game mechanics
        time.sleep(random.uniform(0.1, 0.5))  # simulate gameplay delay
        self.score += random.randint(1, 10)
        print(f'Score: {self.score}')

    def level_up(self):
        self.level += 1
        self.score = 0
        print(f'Level Up! Current Level: {self.level}')

    def stop(self):
        self.is_running = False

if __name__ == '__main__':
    game = GameEngine()
    try:
        game.run()
    except KeyboardInterrupt:
        game.stop()  # Handle graceful exit on interrupt
        print('Game Stopped')