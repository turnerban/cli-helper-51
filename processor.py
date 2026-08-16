import json

class GameDataProcessor:
    def __init__(self, data):
        self.data = data

    def filter_data(self, filter_func):
        return [d for d in self.data if filter_func(d)]

    def convert_to_json(self):
        return json.dumps(self.data, indent=4)

    def aggregate_scores(self):
        return sum(d['score'] for d in self.data if 'score' in d)

    def get_average_score(self):
        score_list = [d['score'] for d in self.data if 'score' in d]
        return sum(score_list) / len(score_list) if score_list else 0.0

if __name__ == '__main__':
    sample_data = [
        {'player': 'Alice', 'score': 200},
        {'player': 'Bob', 'score': 150},
        {'player': 'Charlie', 'score': 300}
    ]
    processor = GameDataProcessor(sample_data)
    print(processor.convert_to_json())
    print('Total score:', processor.aggregate_scores())
    print('Average score:', processor.get_average_score())