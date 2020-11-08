import csv
from Utilities.absolute_path import absolute_path
from Utilities.type_checker import is_valid_number

class CSVReader:
    data = []

    def __init__(self, filepath):
        self.data = []

        with open(absolute_path(filepath)) as text_data:
            csv_data = csv.DictReader(text_data, delimiter=',')
            for row in csv_data:
                for k, v in row.items():
                    num = v
                    is_valid_number(num)
                self.data.append(row)
        pass