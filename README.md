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
Jupyter Notebook: top10.ipynb (additional feature: movie posters)
```
> For performance purposes, we are using the database of 5000 movies, an extract of the much bigger database.

Using the `tmdb_5000_movies.csv` database, the user is asked to input genre(s) (up to five different genres: Action, Adventure, Romance etc.) and era(s) (up to five, from the 10s to late 2010) and the program will display a table showing movie titles, average score by users from TMDB and list of genre(s) thanks to tabulate library.
If run on Jupyter Notebook, the rest of the code will display a table in HTML format with the addition of movie posters taken from IMDB website.

### Webinterface
```
movieselector.py
selectmoviebis.html
style.css
action.png, adventure.png, crime.png, western.png, war.png, mystery.png, tvmovie.png, thriller.png, music.png, horror.png, history.png, romance.png, drama.png, animation.png, documentary.png, family.png, fantasy.png, foreign.png, comedy.png
```
> We use also the database `tmdb_5000_movies.csv` of 5000 movies.

By running this code, it will display a web interface which asks the user to choose one genre and returns the ten best movies in this genre in the database.

> Science Fiction and TV Movie do not work because of the space separating the two words.

### Prediction model

> For more accuracy, we are using the full database of +350,000 movies
> Merging with casting details from another database causes the program to run for too long to be processed. We decided against complicating our model with casting details despite their relevance and importance.
> Some parameters that may seem relevant were discarded as it takes way too long to process. 

Using the `AllMoviesDetailsCleaned.csv` database, we designed two prediction models using the scikit library. 
1. Model predicting revenue
2. Model predicting if the movie will be a success (average score by users > 5 out of 10): 1 or 0 value


#### Model parameters
The model chosen is the Random Forest Classifier from scikit library.
Parameters determining the outcome of the predictions are:
* adult (if the movie audience is not children): boolean value
* budget: numerical value
* genres
* original language: string of character
* release date (YYYY-MM-DD): it is common knowledge the month and weekday of the movie release greatly influence its success
* runtime

To predict following outcomes:
* revenue: we did not take into account inflation
* vote average

#### Preprocessing

- Categorical values were transformed into numerical values (1 or 0) thanks to functions like get_dummies from pandas.
- Date values were analysed thanks to datetime library, we extracted the year, the month and the weekday of the release date.
- Boolean values were transformed into numerical values thanks to LabelBinarizer() function in the preprocessing package of scikit library.
- Values stored in json format (genres) were first transformed into lists then into numerical values.



## Deployment

We are running Python 3.7.
Errors can be found in the web interface and the second predictive model.

## Authors

* **Caroline Chen** 
* **Tom Didier** 
* **Valentin Karimpour** 

## License

This project is licensed under the ESSEC license

## Acknowledgments

* Python Programming class



