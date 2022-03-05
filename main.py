import pandas as pd
import numpy as np

data = pd.read_csv(r"E:\\Python\DATASETS\\ml-latest-small\\ratings.csv", usecols=['movieId', 'rating'])
data.sort_values(by=['movieId'], inplace=True, ignore_index=True)
print(data.head())


# FIND THE AVERAGE RATING ACCORDING TO NO. OF USERS

movie_ratings = data.groupby(['movieId']).mean()
print(movie_ratings)