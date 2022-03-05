import pandas as pd


# In[41]:


movie_ratings = pd.read_csv('ratings.csv', usecols=['movieId', 'rating'])
movie_ratings


# In[42]:


movie_ratings.sort_values(by='movieId')


# In[43]:


movie_ratings = movie_ratings.groupby(['movieId']).mean()
movie_ratings


# In[44]:


movies = pd.read_csv('movies.csv', index_col='movieId')
movies


# In[52]:


import difflib as dl
genre = input("Enter the preferred Genre : ")
genre_list = ['Action', 'Adventure', 'Animation', "Children's", 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 
              'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
if genre not in genre_list:
    genre = dl.get_close_matches(genre, genre_list, n=1)
genre


# In[53]:


genre = ''.join(genre)
genre


# In[72]:


movies_by_genre = movies.loc[movies['genres'].str.find(genre) != -1]
movies_by_genre.drop(columns='FOUND', inplace=True)


# In[75]:


print("ENTER THE RANGE OF YEAR")
lower_year = int(input("YEAR LOWER BOUND : "))
upper_year = int(input("YEAR UPPER BOUND : "))


# In[77]:


YEAR_LIST = range(lower_year,upper_year)
YEAR_LIST


# In[84]:


def YEAR_FILTER(year):
    movie = movies_by_genre.loc[movies_by_genre['title'].str.find(str(year)) != -1]
    return movie
movie_list = []
for x in YEAR_LIST:
     movie_list.append(YEAR_FILTER(x))
movies = pd.concat(movie_list)
movies


# In[98]:


movie_final = pd.merge(movie_ratings,movies, left_index=True, right_index=True)
movie_final.sort_values(by='rating', ascending=False)
movie_selected = int(input("ENTER THE MOVIE ID : "))
print(movie_final.loc[movie_selected])


# In[ ]:




