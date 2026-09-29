import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"}, "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"}, "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"}, "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"}, "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"}, "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"}, "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"}, "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"}, "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"}, "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"}, "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

# Этап 1. Числа и math
def average_rating(movies_list: list) -> float:
    return round(sum(m["rating"] for m in movies_list) / len(movies_list), 1)

def catalog_age_stats(movies_list: list, current_year: int = 2026) -> tuple:
    ages = [current_year - m["year"] for m in movies_list]
    max_age = max(ages)
    min_age = min(ages)
    avg_age = math.ceil(sum(ages) / len(ages))
    return max_age, min_age, avg_age

def duration_in_hours(minutes: int) -> str:
    return f"{minutes // 60}ч {minutes % 60}м"


def rating_tier(rating: float) -> str:
    if rating >= 9:
        return "шедевр"
    if rating >= 7:
        return "хорошо"
    return "средне" if rating >= 5 else "слабо"

def decade_label(year: int) -> str:
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _:
            return "старые"
def demo_non_comedy(movies_list: list) -> None:
    for m in movies_list:
        if "comedy" in m["genres"]:
            continue
        print(m["title"])

def find_masterpiece(movies_list: list) -> str:
    i = 0
    while i < len(movies_list):
        if movies_list[i]["rating"] > 9.0:
            return movies_list[i]["title"]
        i += 1
    else:
        return "Шедевров не найдено"

def count_long_movies(movies_list: list, threshold: int = 120) -> int:
    count = 0
    for m in movies_list:
        if m["duration_min"] > threshold:
            count += 1
    return count

def normalize_title(title: str) -> str:
    words = title.split(" ")
    result = []
    for word in words:
        if word:
            result.append(word[0].upper() + word[1:])
    return " ".join(result)

def make_slug(title: str) -> str:
    return title.lower().replace(" ", "-")

def format_report_line(movie: dict) -> str:
    title = normalize_title(movie["title"])
    genres_str = ", ".join(sorted(list(movie["genres"])))
    return f'"{title}" ({movie["year"]}) — {movie["rating"]}/10, {duration_in_hours(movie["duration_min"])}, жанры: {genres_str}'

def titles_sorted_by_rating(movies_list: list) -> list:
    return [m["title"] for m in sorted(movies_list, key=lambda x: x["rating"], reverse=True)]

def top_n_by_rating(movies_list: list, n: int = 3) -> list:
    sorted_movies = sorted(movies_list, key=lambda x: x["rating"], reverse=True)
    return [(m["title"], m["rating"]) for m in sorted_movies[:n]]

def count_by_genre(movies_list: list) -> dict:
    counts = {}
    for m in movies_list:
        for genre in m["genres"]:
            counts[genre] = counts.get(genre, 0) + 1
    return counts

def actor_filmography(movies_list: list) -> dict:
    filmography = {}
    for m in movies_list:
        for actor in m["actors"]:
            if actor not in filmography:
                filmography[actor] = []
            filmography[actor].append(m["title"])
    return filmography

def high_rated_dict(movies_list: list) -> dict:
    avg = average_rating(movies_list)
    return {m["title"]: m["rating"] for m in movies_list if m["rating"] > avg}