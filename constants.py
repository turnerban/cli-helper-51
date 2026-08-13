import time
import random

# Constants for retry logic
RETRY_COUNT = 3
RETRY_DELAY_BASE = 1  # in seconds

def exponential_backoff(retry_attempt):
    return RETRY_DELAY_BASE * (2 ** retry_attempt) + random.uniform(0, 1)


def retry_network_operation(func, *args, **kwargs):
    attempts = 0
    while attempts < RETRY_COUNT:
        try:
            return func(*args, **kwargs)
        except Exception as e:
            attempts += 1
            if attempts < RETRY_COUNT:
                delay = exponential_backoff(attempts)
                print(f'Retrying in {delay:.2f} seconds...')
                time.sleep(delay)
            else:
                print(f'Operation failed after {attempts} attempts: {e}') 
                raise

