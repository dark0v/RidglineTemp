import pandas as pd
import matplotlib.pyplot as plt
from joypy import joyplot
from pandas.api.types import CategoricalDtype

df = pd.read_csv('./Data-Analysis/Graphs/Notebooks/Temperatures-Sydney/weatherAUS.csv',usecols=['Date','Location', 'MinTemp', 'MaxTemp'])

# Reading the csv file with temperatures
sydney = df.query("Location == 'Sydney'")
sydney = sydney.drop('Location', axis=1)
sydney['Date'] = sydney['Date'].astype('datetime64')
sydney['Month'] = sydney['Date'].dt.month_name()

cat_month = CategoricalDtype(
    ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
)

sydney['Month'] = sydney['Month'].astype(cat_month)
plt.figure()

# Generating ridgline graph
ax, fig = joyplot(
    data=sydney[['MinTemp', 'MaxTemp', 'Month']], 
    by='Month',
    column=['MinTemp', 'MaxTemp'],
    color=['#686de0', '#eb4d4b'],
    legend=True,
    alpha=0.90,
    linewidth=0.55,
    figsize=(12,10),
)

plt.title('Ridgline Test to show Min and Max Temperatures in Sydney', fontsize=20)

# Export ridgline graph to a png file in the same directory
plt.savefig(r'./Data-Analysis/Graphs/Notebooks/Temperatures-Sydney/Ridgline-TempSydney.png',bbox_inches="tight" )