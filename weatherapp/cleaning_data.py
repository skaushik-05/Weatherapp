import pandas as pd
import itertools
import os
os.chdir('C:/Users/Shubham Kaushik/projects/workproject/weatherapp/weatherapp/')
df = pd.read_csv('Final_wunderground.csv')
latlong = pd.read_csv('latlongmapping.csv')
df = (df.set_index(['geocode'])
   .apply(lambda x: x.str.split(',').explode())
   .reset_index())     
df['date']= df['validTimeLocal'].apply(lambda x: x[:10])
df['date'] = pd.to_datetime(df['date']) 
df = df[(df['date']!=max(df['date']))& (df['date']!=min(df['date']))]
lst = df.geocode.values[0].split('),')
df['geocode']= (list(itertools.chain.from_iterable(itertools.repeat(x, 336) for x in lst)))
df['geocode'] = df['geocode'].apply(lambda x: x.replace("[(", "")).apply(lambda x: x.replace(")]", "")).apply(lambda x: x.replace("(", "")).apply(lambda x: x.replace(" ", ""))
df = pd.merge(df,latlong,left_on='geocode',right_on='lat_long', how='left')
df = df[['geocode','State', 'Code', 'City','validTimeLocal', 'date', 'cloudCover', 'dayOfWeek', 'dayOrNight',
       'pressureMeanSeaLevel', 'qpf', 'qpfSnow', 'relativeHumidity',
       'temperature', 'temperatureDewPoint', 'visibility', 'windSpeed',
       'windDirection', 'windGust', 'wxPhraseLong', 'precipChance',
       'precipType']]
df.to_csv('150DMAs_scrapped.csv')