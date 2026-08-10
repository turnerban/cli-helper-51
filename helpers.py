import os
import json

class FileHelper:
    @staticmethod
    def read_json(file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"{file_path} does not exist.")
        with open(file_path, 'r') as file:
            return json.load(file)

    @staticmethod
    def write_json(file_path, data):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

class StringHelper:
    @staticmethod
    def capitalize_words(string):
        return ' '.join(word.capitalize() for word in string.split())

    @staticmethod
    def reverse_string(string):
        return string[::-1]


if __name__ == '__main__':
    # Sample usage
    sample_data = {'key': 'value'}
    FileHelper.write_json('sample.json', sample_data)
    print(FileHelper.read_json('sample.json'))
    print(StringHelper.capitalize_words('hello world'))
    print(StringHelper.reverse_string('hello'))