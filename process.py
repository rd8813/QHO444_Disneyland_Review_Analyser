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

def get_top_locations_by_rating(data, park):
    location_ratings = {}

    for row in data:
        if row["Branch"] == park:
            location = row["Reviewer_Location"]
            rating = int(row["Rating"])

            if location not in location_ratings:
                location_ratings[location] = []

            location_ratings[location].append(rating)

    averages = []

    for location, ratings in location_ratings.items():
        avg = sum(ratings) / len(ratings)
        averages.append((location, avg))

    averages.sort(key=lambda x: x[1], reverse=True)

    return averages[:10]

def get_monthly_average_ratings(data, park):
    month_ratings = {}

    for row in data:
        if row["Branch"] == park:

            parts = row["Year_Month"].split("-")

            if len(parts) < 2:
                continue

            month = int(parts[1])
            rating = int(row["Rating"])

            if month not in month_ratings:
                month_ratings[month] = []

            month_ratings[month].append(rating)

    averages = []

    for month in range(1, 13):

        if month in month_ratings:
            avg = sum(month_ratings[month]) / len(month_ratings[month])
        else:
            avg = 0

        averages.append(avg)

    return averages