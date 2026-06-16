import matplotlib.pyplot as plt


def show_reviews_by_park_chart(data):
    park_counts = {}

    for row in data:
        park = row["Branch"]

        if park in park_counts:
            park_counts[park] += 1
        else:
            park_counts[park] = 1

    parks = list(park_counts.keys())
    counts = list(park_counts.values())

    plt.pie(counts, labels=parks, autopct="%1.1f%%")
    plt.title("Number of Reviews by Park")
    plt.show()

def show_top_locations_chart(locations, ratings, park):
    plt.figure(figsize=(10, 5))
    plt.bar(locations, ratings)
    plt.title(f"Top 10 Locations by Average Rating - {park}")
    plt.xlabel("Location")
    plt.ylabel("Average Rating")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def show_monthly_ratings_chart(months, ratings, park):
    plt.figure(figsize=(10, 5))
    plt.bar(months, ratings)
    plt.title(f"Average Monthly Rating - {park}")
    plt.xlabel("Month")
    plt.ylabel("Average Rating")
    plt.tight_layout()
    plt.show()