# statistics.py

def calculate_stats(library):
    total = len(library)
    read_count = sum(1 for book in library if book["read"])
    percentage_read = (read_count / total) * 100 if total > 0 else 0
    return total, read_count, percentage_read

def average_rating(library):
    ratings = [book["rating"] for book in library if book["read"] and book["rating"]]
    if ratings:
        return sum(ratings) / len(ratings)
    return None
 # type: ignore