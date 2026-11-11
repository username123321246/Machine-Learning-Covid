import pandas as pd
import matplotlib as plt
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

asd = pd.read_csv("LESSONS\\covid_data.csv")
print(asd.head())

asd = asd[["Province_State", "Country_Region", "Confirmed", "Recovered", "Deaths", "Active", "Lat", "Long_"]]
asd.columns = ("State", "Country", "Confirmed Cases", "Recovered Cases", "Deaths", "Active Cases", "Latitude", "Longitude")
print(asd.head())

asd["State"] = asd["State"].fillna("")
print(asd.head())

top_ten_countries = pd.DataFrame(asd.groupby("Country") ["Confirmed Cases"].sum().nlargest(10).sort_values(ascending = False))
Fig1 = px.scatter(top_ten_countries, x = top_ten_countries.index, y = "Confirmed Cases", size = "Confirmed Cases", size_max = 200, color = top_ten_countries.index)
Fig1.write_html("Figure.html", auto_open = True)




