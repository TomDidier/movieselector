import pandas as pd
import ast
from tabulate import tabulate
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import sklearn
from sklearn import linear_model

#Importation de la base de données et filtrage des genres possibles 
movies = pd.read_csv("C:/Users/Valentin/Documents/1. ESSEC/1. Cours/4. 4A/1. Python/2. FINAL (tests)/tmdb_5000_movies.csv", delimiter= ",")
movies['genres'] = [list(set([y['name'] for y in x])) for x in movies['genres'].apply(ast.literal_eval)]
genre_possible = set(x for l in movies["genres"] for x in l)
print(genre_possible)

#Conversion des colonnes de la nouvelle dataframe en liste
budget_list = movies['budget'].tolist()
vote_average_list = movies['vote_average'].tolist()

#Calcul des paramètres nécessaires pour faire une droite de régression linéaire
def slope_intercept(x_val,y_val):
    x = np.array(budget_list)
    y = np.array(vote_average_list)
    m = (np.mean(x)*np.mean(y) - np.mean(x*y)) / (np.mean(x)*np.mean(x) - np.mean(x*x))
    m = round(m,2)
    b = np.mean(y) - np.mean(x)*m
    b = round(b,2)
    return m,b
test = slope_intercept(budget_list, vote_average_list)
m,b = test
reg_line = [(m*x)+b for x in  budget_list]

#Mise en forme d'un scatter plot de façon à visualiser une éventuelle corrélation entre le budget investi et la note des spectateurs
plt.scatter(budget_list, vote_average_list, color = 'red')
plt.plot(budget_list, reg_line)
ylab = 'Average Public Vote'
xlab = 'Budget spent'
title = 'Budget to public reaction correlation'
plt.ylabel(ylab) 
plt.xlabel(xlab) 
plt.title(title)
plt.yticks([0, 1, 2, 3 , 4, 5, 6, 7, 8, 9, 10])
xticks_val = [0, 50000000, 100000000 , 150000000, 200000000, 250000000, 300000000, 350000000, 400000000, 450000000]
xticks_lab = ["0", "50M", "100M", "150M", "200M", "250M", "300M", "350M", "400M", "450M"]
plt.xticks(xticks_val, xticks_lab)
plt.show()


