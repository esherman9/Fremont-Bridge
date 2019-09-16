import os
from urllib.request import urlretrieve
import pandas as pd

URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

def get_data(filename='Fremont.csv', url=URL):
    if not os.path.exists(filename):
        urlretrieve(url, filename)
    data = pd.read_csv('Fremont.csv', index_col = 'Date', parse_dates=True)
    #data[data['Date'] > 2017]
    data.columns = ['West','East']
    data['Total'] = data['West'] + data['East']
    return data
