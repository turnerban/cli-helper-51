import random
import logging

class Processor:
    def __init__(self):
        self.data = []
        self.log = logging.getLogger("Processor")

    def add_data(self, item):
        if not isinstance(item, int):
            self.log.error("Item must be an integer, got %s", type(item).__name__)
            raise ValueError("Item must be an integer")
        self.data.append(item)
        self.log.info("Added item: %d", item)

    def compute_average(self):
        if not self.data:
            self.log.warning("No data available to compute average")
            raise ValueError("No data available")
        average = sum(self.data) / len(self.data)
        self.log.info("Computed average: %.2f", average)
        return average

    def get_random_item(self):
        if not self.data:
            self.log.error("Attempted to retrieve from empty data list")
            raise IndexError("The data list is empty")
        item = random.choice(self.data)
        self.log.info("Retrieved random item: %d", item)
        return item
