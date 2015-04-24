from pandas import *
from ggplot import *
import pprint

import datetime
import itertools
import operator

import brewer2mpl
import ggplot as gg
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pylab
import scipy.stats
import statsmodels.api as sm

#%matplotlib inline
#ggplot.colors.COLORS.extend(["#ff0000", "#00ff00", "#0000ff"])

def plot_weather_data(tw):
#  plot=ggplot(aes(y='ENTRIESn_hourly',x='Hour'), data=tw) \
#    +geom_point(color='lightblue')+stat_smooth(span=.15,color='black',se=True) \
#    +xlab("Hour")+ylab("ENTRIESn_hourly")+ggtitle("T")
#  plot=ggplot(aes(x='ENTRIESn_hourly'), data=tw)+geom_density() \
#    +xlab("ENTRIESn_hourly")+ylab("Density")+ggtitle("T")
#  plot=ggplot(tw,aes(x='EXITSn_hourly',y='ENTRIESn_hourly', color='rain')) \
#    +geom_point()+xlab("X")+ylab("Y")+ggtitle("T")
#  plot=ggplot(tw,aes(x='EXITSn_hourly', fill='ENTRIESn_hourly')) \
#    +geom_density(alpha=0.25)+facet_wrap("grp")
#  plot=ggplot(tw,aes(x='EXITSn_hourly', fill='grp'))+geom_density(alpha=0.25)
  #ggsave(plot, "abc.png")
#  return plot

  df = turnstile_weather.copy()
  
  #
  df['datetime'] = df.loc[:,'DATEn'].map(lambda x: pandas.to_datetime(x))
  df['dayofweek'] = df.loc[:,'datetime'].map(lambda x: x.strftime('%A'))
  # print df['dayofweek']
  
  # print df['ENTRIESn_hourly'].describe()
  df['entries_log'] = np.log10(df['ENTRIESn_hourly'].fillna(0) + 1)
  
  #plot = ggplot(turnstile_weather, aes('EXITSn_hourly', 'ENTRIESn_hourly')) \
  #  + stat_smooth(span=.15, color='black', se=True)+ geom_point(color='lightblue') \
  #  + ggtitle("MTA Entries By The Hour!") \
  #  + xlab('Exits') + ylab('Entries')
  #plot = ggplot(df, aes('entries_log')) \
  #  + geom_histogram() \
  #  + facet_wrap('rain') \
  #  + ggtitle("Histogram log10(entries by hour). Rain No-Rain") \
  #  + xlab('Entries per hour') #+ ylab('Entries')
  #df_group = df.groupby('dayofweek', as_index=False).sum()
  #print df_group
  #plot = ggplot(df_group, aes(x='dayofweek', y='ENTRIESn_hourly')) \
  #   + geom_bar(stat='bar') \
  #   + ggtitle("Entries by day of week") \
  #   + xlab('Day of week') + ylab('Entries') #+ scale_x_date(labels = date_format("%d"))
  #df_group = df.groupby('Hour', as_index=False).sum()
  #print df_group
  #plot = ggplot(df_group, aes(x='Hour', y='ENTRIESn_hourly')) \
  #  + geom_bar(stat='bar') \
  #  + ggtitle("Entries by hour") \
  #  + xlab('Hour') + ylab('Entries') #+ scale_x_date(labels = date_format("%d"))
  df_group = df.groupby(['Hour', 'rain'], as_index=False).median()
  df_group.to_csv('dump.csv')
  plot = ggplot(df_group, aes(x='Hour', y='ENTRIESn_hourly', color='rain')) \
    + geom_line() \
    + ggtitle("Entries median by hour of day, red=rain blue=no rain") \
    + xlab('Hour') + ylab('Median of ENTRIESn') \
    + scale_x_continuous(breaks=range(0,24,2))
  
#  plot = df.describe()
  return plot

if __name__ == "__main__":
    image = "plot.png"
    input_filename = 'C:/move - bwlee/Data Analysis/Nano/Intro to Data Science/project/code/turnstile_data_master_with_weather.csv'
    # with open(image, "wb") as f:
    turnstile_weather = pandas.read_csv(input_filename)
    turnstile_weather['datetime']=turnstile_weather['DATEn']+' '+turnstile_weather['TIMEn']
    gg=plot_weather_data(turnstile_weather)
    print gg
#    ggsave(f, gg)

