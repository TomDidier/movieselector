
#####################
#                   #
# PREDICTION MODEL  #
#                   #
#####################

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn import preprocessing 
import numpy as np
import pandas as pd
import ast
import seaborn as sn #to plot beautiful confusion matrix
import matplotlib.pyplot as plt

#Working on the bigger dtb (+50k movies)
allmovies = pd.read_csv("Groupwork/movies_metadata.csv")

#Keeping relevant columns from df
#No production company because it takes too long to process as one hot encoder
df3 = allmovies[['title','adult', 'budget', 'genres', 
'id', 'original_language','release_date', 'revenue', 'runtime', 'vote_average']]

#Drop rows where NAs
df3 = df3.dropna()

#Cleaning
#Transform the json format into a simple list
df3['genres'] = [list(set([y['name'] for y in x])) for x in df3['genres'].apply(ast.literal_eval)]
#df3['production_companies'] = [list(set([y['name'] for y in x])) for x in df3['production_companies'].apply(ast.literal_eval)]

df3['title'] = df3['title'].astype('str')
df3["vote_average"].fillna("0", inplace=True)
df3['vote_average'] = df3['vote_average'].astype('float')
df3['runtime'] = df3['runtime'].astype('float')

#Date information (same code as first part)
df3["release_date"] = pd.to_datetime(df3["release_date"])
df3['year'] = df3['release_date'].dt.year
df3['month'] = df3['release_date'].dt.month
df3['weekday'] = df3['release_date'].dt.weekday #Return the day of the week as an integer, where Monday is 0 and Sunday is 6.

df3['budget'] = pd.to_numeric(df3['budget'], errors='coerce')
lb = preprocessing.LabelBinarizer()
df3[["adult"]] = lb.fit_transform(df3[["adult"]]) #True = 1 and False = 0

list_genre = set(x for l in df3["genres"] for x in l)
print(list_genre)

#get_dummies from pd replace categorical values with their One Hot encoder equivalent (numerical values, 0 or 1)
cols_to_transform = [ 'original_language', 'year', 'month','weekday']
new_df3 = pd.get_dummies(df3, columns = cols_to_transform )
#Cleaning the genre columns so it becomes a one hot encoder column
new_df3 = pd.concat([new_df3, pd.get_dummies(new_df3.genres.apply(pd.Series).stack()).sum(level=0)], axis = 1)

#dropping unecessary columns
final_df3 = new_df3.drop(columns=["release_date", "id", "genres", "title"])
final_df3 = final_df3.dropna()

#Model 1: how much the movie will generate in revenue
#Training and fitting the model
#Using a scikit.model selection function to randomly select a train and test dataframe
X, y = final_df3.drop('revenue', axis=1), final_df3['revenue']
X_train, X_test, Y_train, Y_test = train_test_split(X, y, train_size=0.60, test_size=0.40)

rf = RandomForestClassifier(n_estimators = 150, max_depth=5)
rf.fit(X_train, Y_train)
Y_pred = rf.predict(X_test) #very long to run
rf.score(X_train, Y_train) #very long to calculate. Output is 0.82 

#Model 2: what will be its average score on TMDB
#0 or 1 if the movie is considered a success (average_score > 5)
final_df3.loc[df3.vote_average > 5, 'is_success'] = 1
final_df3.loc[df3.is_success.isnull()] = 0
final_df3['is_success'] = final_df3['is_success'].astype('int')

final_df3 = final_df3.dropna()

X, y = final_df3.drop('is_success', axis=1), final_df3['is_success']
X_train, X_test, Y_train, Y_test = train_test_split(X, y, train_size=0.60, test_size=0.40)

rf = RandomForestClassifier(n_estimators = 150, max_depth=5)
rf.fit(X_train, Y_train)
Y_pred = rf.predict(X_test) #very long to run
rf.score(X_train, Y_train) #problem with prediction

#Confusion matrix to see false positive, false negative and right results
cf =confusion_matrix(Y_test,Y_pred)
print(cf)