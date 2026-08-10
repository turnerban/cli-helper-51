def safe_divide(numerator, denominator):
    """Safely divides numerator by denominator, handling edge cases."""
    try:
        if denominator == 0:
            raise ValueError('Denominator cannot be zero.')
        return numerator / denominator
    except TypeError:
        raise TypeError('Both numerator and denominator must be numbers.')


def read_file(file_path):
    """Reads content from a file, with error handling for edge cases."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f'File not found: {file_path}')
    except IOError:
        raise IOError('An error occurred trying to read the file.')


def parse_int(value):
    """Tries to parse a string to an integer with error handling."""
    try:
        return int(value)
    except ValueError:
        raise ValueError(f'Value must be an integer: {value}')
    except TypeError:
        raise TypeError('Input must be a string or a number.')