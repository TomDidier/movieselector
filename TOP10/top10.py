import pandas as pd
import ast
import re
import json
import datetime
from tabulate import tabulate
from IPython.display import Image, HTML

#very important line of code so that HTML tables are displayed correctly
pd.set_option('display.max_colwidth', -1)

movies = pd.read_csv("Groupwork/tmdb_5000_movies.csv", delimiter= ",")
allmovies = pd.read_csv("Groupwork/movies_metadata.csv")

#####################
#                   #
# CLEANING          #
#                   #
#####################

#converting the columns that are into json format into a simple list thanks to library ast
movies['genres'] = [list(set([y['name'] for y in x])) for x in movies['genres'].apply(ast.literal_eval)]
movies['id'] = movies['id'].astype('float')
allmovies = allmovies[~allmovies.id.str.contains("-")] #drop rows where wrogn id format (like date!)
allmovies['id'] = allmovies['id'].astype('float')
movies = pd.merge(movies, allmovies[['id','poster_path']],on='id', how='left')

#Get list of all the genres possible for a movi
genre_possible = set(x for l in movies["genres"] for x in l)
#print(genre_possible)

#Create a column "decade" on your dataframe
movies["release_date"] = pd.to_datetime(movies["release_date"])
movies['year'] = movies['release_date'].dt.year
def release_decade(c):
    if c["year"] >1999 and c["year"] < 2010:
        return 2000
    elif c["year"] >= 2010:
        return 2010
    else:
        return (c["year"] - ((c["year"]//100)*100))//10*10

#Be careful: run the command step by step to avoid errors
movies['decade'] = movies.apply(release_decade, axis=1)
movies.loc[movies['decade'].isnull()] #see where value is na, only one movie is affected
movies["decade"].fillna("2010", inplace=True)
#movies.loc[movies['decade'].isnull()] #empty df so there is no longer a problem

#####################
#                   #
# MODEL             #
#                   #
#####################

#Loop to get what genres the user is interested in
genres_choisi=[]
while True:    # infinite loop
    try:
        element = input("What movie genre interests you (Press Q to stop)? ")
        if element.upper() == "Q":
            break  # stops the loop
        elif element.lower().capitalize() in genres_choisi: #remove duplicates
            print("This genre is already specified!")
            pass
        elif element.lower().capitalize() not in genre_possible: #Check if a chosen genre does exist in our database, if not remove it from our list and ask the user to input a new one or no
            print(element, " is not a valid genre, please choose from", *genre_possible)
            ajouter = input("Do you want to input a new genre? (Y/N) ")
            if ajouter.upper() == "Y":
                genres_choisi.append(input("What genre exactly?").lower().capitalize())
            else:
                break
        else:
            genres_choisi.append(element.lower().capitalize())
    finally:
        print("You're interested in ", *genres_choisi, sep = "\n")
    if len(genres_choisi) > 5:
        print("Too many genres! We'll keep", *genres_choisi)
        break

#Loop to get what decades the user is interested in
decade_choisi = []
while True:    # infinite loop
    try:
        element = int(input("Which decade interests you (Press 0 to stop)? "))
        if element == 0:
            break  # stops the loop
        elif element in decade_choisi: #remove duplicates
            print("This decade is already specified!")
            pass
        else:
            decade_choisi.append(element)
    except ValueError:
        print("Input a number (10,20,..., 2000, 2010) please!")
    finally:
        print("You're interested in movies from era(s):", *decade_choisi, sep = "\n")
    if len(decade_choisi) > 5:
        print("You've already chosen 5 decades! We'll keep", *decade_choisi)
        break

decade_choisi = [float(x) for x in decade_choisi]

#get the poster image
movies['poster_path2'] = "<img src='http://image.tmdb.org/t/p/w185"+movies["poster_path"]+"' style='height:100px;'>"

#Dataframe with only movies in selected decade
df1 = movies[movies['decade'].isin(decade_choisi)]

#Générer une dataframe correspondant aux genres voulus 
df2 = df1[[all(x in y for x in genres_choisi) for y in df1["genres"].values]]

#Sort movies based on score calculated above and print a beautiful table of the TOP10
df2 = df2.sort_values('vote_average', ascending=False)

#Tabulate table
print("Out of", str(len(df1.index)), "movies meeting your criteria, here's the top 10..." )
print(tabulate(df2[['title', "year", 'vote_average']].head(10), headers=["Movie", "Year","Average score"], showindex="never", tablefmt="fancy_grid"))

#HTML table
htmltable2 = df2[["poster_path2","title", "vote_average", "genres"]].head(10)
display(HTML(htmltable2.to_html(escape = False, index = False)))