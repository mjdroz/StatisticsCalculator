import csv
from Utilities.absolute_path import absolute_path

class CSVReader:
    data = []

    def __init__(self, filepath):
        self.data = []

        with open(absolute_path(filepath)) as text_data:
            csv_data = csv.DictReader(text_data, delimiter=',')
            for row in csv_data:
                self.data.append(row)
        pass