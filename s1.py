import pkg_resources
pkg_resources.require("matplotlib==1.4.0")
from pandas import *
from ggplot import *
import pprint
import csv
import itertools

import ggplot as gg
import numpy as np
import pandas as pd
from datetime import datetime, date, time
import matplotlib.pyplot as plt

turnstile_weather=pandas.read_csv("C:/move - bwlee/Data Analysis/Nano/\
Intro to Data Science/project/code/turnstile_data_master_with_weather.csv")

plot=ggplot(turnstile_weather,aes(x='ENTRIESn_hourly',y='EXITSn_hourly',color='Hour')) \
+ geom_point() \
+ scale_color_brewer(type='diverging', palette=4) \
+ xlab("Entries") \
+ ylab("Exits")\
+ ggtitle("Entries vs Exists by hour")
#print plot

df = DataFrame({"rain": turnstile_weather[turnstile_weather['rain']==1]['ENTRIESn_hourly'], \
  "no_rain": turnstile_weather[turnstile_weather['rain'] == 0]['ENTRIESn_hourly']}).fillna(0)
df = melt(df)
plot = ggplot(aes(x='value', color='variable'), data=df) \
  + geom_histogram(binwidth=400) \
  + scale_y_log() \
  + ylab("Frequency") \
  + xlab("Entries Per Hour")\
  + ggtitle("Entries Per Hour vs Frequency")
#print plot

df = DataFrame({"rain": turnstile_weather[turnstile_weather['rain']==1]['ENTRIESn_hourly'], \
  "no_rain": turnstile_weather[turnstile_weather['rain'] == 0]['ENTRIESn_hourly']})
df.to_csv('dump1.csv')
df = melt(df)
df.to_csv('dump2.csv')
#print df

plot=ggplot(aes(x='value',fill='variable'),data=df) \
+geom_histogram(binwidth=1000) \
+scale_y_log() \
+ylab("Frequency of Log 10 scale") \
+xlab("Number of Entries")\
+ggtitle("Frequency of Hourly Entry, red=No rain, blue=rain")
print plot