def load_data(file_path):
    data = []
    return data

import csv


def load_data(file_path):
    data = []

    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            data.append(row)

    return data