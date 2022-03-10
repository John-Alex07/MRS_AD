import pandas as pd
import Ratings_Preprocessing

user_movie = Ratings_Preprocessing.movie_selected
tags = pd.read_csv("E:\\Python\\DATASETS\\ml-latest-small\\tags.csv", index_col='movieId', usecols=['movieId','tag'])
print(tags.head())