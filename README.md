# Movie selector

A project to get the ten best movies in one genre, from chosen period of time, out of a database of 5000 movies from The Movie Database API, thanks to a web interface.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites
#### Sources
Two databases need to be install from Kaggle:

| Databases     | Usages        
| ------------- |:-------------:| 
| [Metadata on 5,000 movies from TMDB](https://www.kaggle.com/tmdb/tmdb-movie-metadata)    | Web interface, TOP10, graphs | 
| [350 000+ movies from themoviedb.org](https://www.kaggle.com/stephanerappeneau/350-000-movies-from-themoviedborg)      | Prediction model      | 

#### Softwares
Softwares and libraries used:

1. Python 3.7:
* Pandas
* Ast
* Tabulate
* Matplotlib
* Numpy
* Scipy
* Sklearn
* IPython.display

2. Visual Studio Code

3. Jupyter Notebook

It is advised to run the script top10.py on Jupyter Notebook.

### Installing

Download the databases from the Prerequisite section

## Project
### Graphs

```
Matplotlib_scatter_plot.py
```
By running this file, you can have an overview of how the budget invested in movies is correlated to the average vote viewers will give. It is a visual representation of the database. The scatter plot shows that the correlation looks like a Gauss curve with an average vote at 6/10

### Displaying the top10 movies from chosen genre(s) and decade(s) 
```
top10.py 
```
> For performance purposes, we are using the database of 5000 movies, an extract of the much bigger database.

Using the `tmdb_5000_movies.csv` database, the user is asked to input genre(s) (up to five different genres: Action, Adventure, Romance etc.) and era(s) (up to five, from the 10s to late 2010) and the program will display a table showing movie titles, average score by users from TMDB and list of genre(s) thanks to tabulate library.
If run on Jupyter Notebook, the rest of the code will display a table in HTML format with the addition of movie posters taken from IMDB website.

> The HTML library is unstable and error for displaying movie posters may occur.

### Webinterface
```
movieselector.py
selectmoviebis.html
style.css
action.png, adventure.png, crime.png, western.png, war.png, mystery.png, tvmovie.png, thriller.png, music.png, horror.png, history.png, romance.png, drama.png, animation.png, documentary.png, family.png, fantasy.png, foreign.png, comedy.png
```
> We use also the database of 5000 movies.

By running this code, it will display a web interface which asks the user to choose one genre and returns the ten best movies in this genre in the database.

> Science Fiction and TV Movie don't work because of the space separating the two words.

### Prediction model

> For more accuracy, we are using the full database

Using the `AllMoviesDetailsCleaned.csv` joined with the `AllMoviesCastingRaw.csv` databases, we dseigned a prediction model using the scikit library.

## Deployment

We are running Python 3.7


## Authors

* **Caroline Chen** 
* **Tom Didier** 
* **Valentin Karimpour** 

## License

This project is licensed under the ESSEC license

## Acknowledgments

* Python Programming class



