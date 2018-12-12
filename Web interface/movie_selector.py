import pandas as pd
import ast
from tabulate import tabulate
from flask import Flask, send_from_directory, render_template
app = Flask(__name__)

movies = pd.read_csv("Projet de groupe/tmdb_5000_movies.csv", delimiter= ",")

movies['genres'] = [list(set([y['name'] for y in x])) for x in movies['genres'].apply(ast.literal_eval)] #converting the columns that are into json format into a simple list thanks to library ast
genres_possibles=movies['genres'].head()
print(genres_possibles)

@app.route('/')
def mainpage():
    return render_template("selectmoviebis.html", newChoice=True, genres={}, selectedfilm=False) #defining the web interface function

@app.route('/choice/<genres_choisis>')
def choixfilm(genres_choisis):
    global movies #calling the dataframe we created out of the function
    genresdico = {"TV Movie":genres_choisis=="TVMovie",
    "Comedy":genres_choisis=="Comedy",
    "Thriller":genres_choisis=="Thriller",
    "War":genres_choisis=="War",
    "Foreign":genres_choisis=="Foreign",
    "Music":genres_choisis=="Music",
    "Animation":genres_choisis=="Animation",
    "Documentary":genres_choisis=="Documentary",
    "Action":genres_choisis=="Action",
    "Science Fiction":genres_choisis=="ScienceFiction",
    "Drama":genres_choisis=="Drama",
    "Adventure":genres_choisis=="Adventure",
    "Mystery":genres_choisis=="Mystery",
    "Western":genres_choisis=="Western",
    "History":genres_choisis=="History",
    "Fantasy":genres_choisis=="Fantasy",
    "Crime":genres_choisis=="Crime",
    "Family":genres_choisis=="Family",
    "Horror":genres_choisis=="Horror",
    "Romance":genres_choisis=="Romance"} #defining a dictionnary with "True" for the genre we chose, so that the application understands what genre we chose (for the HTML)
    genres_choisis=[genres_choisis] #transforming the genre we chose (a string) into a list so that 
    df2 = movies[[all(x in y for x in genres_choisis) for y in movies["genres"].values]] #this function works (it selects the movies in this genre from the dataframe)
    df2 = df2.sort_values('vote_average', ascending=False) #rank movies according to their average rating
    Filmschoisis1=df2['title'].head(10).values.tolist() #select the ten first ones
    Filmschoisis2=", \n".join(Filmschoisis1) #transform the list of movies into a string (the format of selectedfilm)
    return render_template("selectmoviebis.html", newChoice=False, genres=genresdico, selectedfilm=Filmschoisis2) #sending the chosen genres and the selected movies to the html

@app.route('/img/<nom_image>')
def sendImages(nom_image):
    return send_from_directory('static/img', nom_image) #sending the images to the CSS code

@app.route('/style.css')
def sendCSS():
    return send_from_directory('static','style.css') #defining the function for the CSS format

if __name__ == '__main__':
   app.run() #running the web application
