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

def get_reviews_by_park(data, park):
    reviews = []

    for row in data:
        if row["Branch"] == park:
            reviews.append(row)

    return reviews

def get_average_rating_by_park_and_year(data, park, year):
    total_rating = 0
    review_count = 0

    for row in data:
        row_year = row["Year_Month"].split("-")[0]

        if row["Branch"] == park and row_year == year:
            total_rating += int(row["Rating"])
            review_count += 1

    if review_count == 0:
        return 0

    return total_rating / review_count