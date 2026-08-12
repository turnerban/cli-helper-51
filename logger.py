import logging

# Configure logging settings
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Create a logger object
logger = logging.getLogger('cli-helper-51')

# Function to log a message if it's deemed valid

def log_message(message):
    if isinstance(message, str) and message:
        logger.info(message)
    else:
        logger.warning('Invalid message: Must be a non-empty string')

# Main processing loop simulation

def main_loop():
    while True:
        user_input = input('Enter a message to log (or type "exit" to quit): ')
        if user_input.lower() == 'exit':
            break  
        log_message(user_input)

if __name__ == '__main__':
    main_loop()