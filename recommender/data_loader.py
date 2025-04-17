import pandas as pd

def load_data():
    ratings = pd.read_csv("data/ratings.csv")
    movies = pd.read_csv("data/movies.csv")

    data = pd.merge(ratings, movies, on="movieId")
    return data
