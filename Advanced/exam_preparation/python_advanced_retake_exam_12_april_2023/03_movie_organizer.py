def movie_organizer(*movies_data):
    movies = {}

    for movie, genre in movies_data:

        if genre not in movies:
            movies[genre] = []
        movies[genre].append(movie)

    sorted_movies = sorted(movies.items(), key=lambda x: (-len(x[1]), x[0]))

    result = []

    for curr_genre, curr_movies in sorted_movies:
        sorted_curr_movies = sorted(curr_movies)

        result.append(f'{curr_genre} - {len(sorted_curr_movies)}')
        result.extend(f'* {movie}' for movie in sorted_curr_movies)

    return '\n'.join(result)


print(movie_organizer(
    ("The Matrix", "Sci-fi")))

print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))

print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))
