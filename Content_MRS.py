import pandas as pd
import Ratings_Preprocessing

user_movie = Ratings_Preprocessing.movie_selected
tags = pd.read_csv("E:\\Python\\DATASETS\\ml-latest-small\\tags.csv", index_col='movieId', usecols=['movieId','tag'])


user_movie = Ratings_Preprocessing.movie_selected

genre_similar = user_movie.genres
genre_similar = genre_similar.split('|')


def movie_similar(movie_gen):
    if movie_gen != Ratings_Preprocessing.genre:
        movies = Ratings_Preprocessing.movies.loc[Ratings_Preprocessing.movies['genres'].str.find(movie_gen) != -1]
        return movies
    else:
        return


movie_content = []
for gen in genre_similar:
    movie_content.append(movie_similar(gen))

movies_rec = pd.concat(movie_content)
print(movies_rec.head(15))

