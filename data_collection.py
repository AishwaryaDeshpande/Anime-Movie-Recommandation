# -*- coding: utf-8 -*-
"""
Created on Sat Jul 08 12:26:27 2017

@author: Aishu
"""

import pandas as pd 

anime = pd.read_csv("C:\\Users\\Aishu\\Desktop\\My_Projects\\Anime\\anime.csv")
rating = pd.read_csv("C:\\Users\\Aishu\\Desktop\\My_Projects\\Anime\\rating.csv")

anime.dtypes 
rating.dtypes

#Extracting those anime which are movies 
anime_movie = anime[anime["type"]== "Movie"]
anime_movie.head()
anime_movie.dtypes

# merging animue_movie and its user ratings from rating table 

user_movie = pd.merge(rating, anime_movie, on = "anime_id")

# droping not necessary columns 
user_movie.drop(["episodes","type"], axis= 1, inplace = True)
