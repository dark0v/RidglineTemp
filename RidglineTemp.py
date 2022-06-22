import pandas as pd
import matplotlib.pyplot as plt
from joypy import joyplot
from pandas.api.types import CategoricalDtype

df = pd.read_csv('weatherAUS.csv',usecols=['Date','Location', 'MinTemp', 'MaxTemp'])

sydney = df.query("Location == 'Sydney'")
sydney = sydney.drop('Location', axis=1)
sydney['Date'] = sydney['Date'].astype('datetime64')
sydney['Month'] = sydney['Date'].dt.month_name()

cat_month = CategoricalDtype(
    ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
)

sydney['Month'] = sydney['Month'].astype(cat_month)

plt.figure()

ax, fig = joyplot(
    data=sydney[['MaxTemp', 'Month']],
    by='Month',
    figsize=(12,8)
)

plt.title('Ridgline Test to show Max Temperatures in Sydney', fontsize=20)
plt.show()