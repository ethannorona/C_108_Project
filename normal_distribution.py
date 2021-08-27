#Importing necessary modules
import csv
import pandas as pd
import plotly.figure_factory as pf

#Reading the data and setting it to the dataframe from data.csv
df = pd.read_csv("data.csv")

#Fig variable to create a distplot with the data about the Avg Rating from the data frame  |  create_distplot = create distribution plot
fig = pf.create_distplot([df["Avg Rating"].tolist()], ["Avg Rating"])

#Displaying the fig variable/distribution
fig.show()