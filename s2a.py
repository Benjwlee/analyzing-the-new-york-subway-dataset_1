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
#  plot=ggplot(aes(y='ENTRIESn_hourly',x='Hour'), data=tw)+geom_point(color='lightblue')+stat_smooth(span=.15,color='black',se=True)+xlab("Hour")+ylab("ENTRIESn_hourly")+ggtitle("T")
#  plot=ggplot(aes(x='ENTRIESn_hourly'), data=tw)+geom_density()+xlab("ENTRIESn_hourly")+ylab("Density")+ggtitle("T")
#  plot=ggplot(tw,aes(x='EXITSn_hourly',y='ENTRIESn_hourly', color='rain'))+geom_point()+xlab("X")+ylab("Y")+ggtitle("T")
#  plot=ggplot(tw,aes(x='EXITSn_hourly', fill='ENTRIESn_hourly'))+geom_density(alpha=0.25)+facet_wrap("grp")
#  plot=ggplot(tw,aes(x='EXITSn_hourly', fill='grp'))+geom_density(alpha=0.25)
  #ggsave(plot, "abc.png")
  return plot

turnstile_weather=pandas.read_csv("C:/move - bwlee/Data Analysis/Nano/Intro to Data Science/project/code/turnstile_data_master_with_weather.csv")

print turnstile_weather.head(n=3)
turnstile_weather["DATETIMEn"] = pd.to_datetime(turnstile_weather["DATEn"] + " " + turnstile_weather["TIMEn"], format="%Y-%m-%d %H:%M:%S")

turnstile_dt = turnstile_weather[["DATETIMEn", "ENTRIESn_hourly", "EXITSn_hourly"]] \
               .set_index("DATETIMEn") \
               .sort_index()
fig, ax = pylab.subplots(figsize=(12, 7))
set1 = brewer2mpl.get_map('Set1', 'qualitative', 3).mpl_colors
turnstile_dt.plot(ax=ax, color=set1)
ax.set_title("Entries/exits per hour across all stations")
ax.legend(["Entries", "Exits"])
ax.set_ylabel("Entries/exits per hour")
ax.set_xlabel("Date")

turnstile_day = turnstile_dt
turnstile_day["day"] = turnstile_day.index.weekday
turnstile_day = turnstile_day[["day", "ENTRIESn_hourly", "EXITSn_hourly"]] \
            .groupby("day") \
            .agg(sum)

fig, ax = plt.subplots(figsize=(12, 7))
set1 = brewer2mpl.get_map('Set1', 'qualitative', 3).mpl_colors
turnstile_day.plot(ax=ax, kind="bar", color=set1)
ax.set_title("Total entries/exits per hour by day across all stations")
ax.legend(["Exits", "Entries"])
ax.set_ylabel("Entries/exits per hour")
ax.set_xlabel("Day")
ax.set_xticklabels(["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
                   rotation=45)

turnstile_by_hour = turnstile_dt.resample("H")
turnstile_by_hour["hour"] = turnstile_by_hour.index.hour
turnstile_by_hour = turnstile_by_hour[["hour", "ENTRIESn_hourly", "EXITSn_hourly"]] \
            .groupby("hour") \
            .sum()

fig, ax = pylab.subplots(figsize=(12, 7))
set1 = brewer2mpl.get_map('Set1', 'qualitative', 3).mpl_colors
turnstile_by_hour.plot(ax=ax, color=set1)
ax.set_title("Total entries/exits per hour by hour across all stations")
ax.legend(["Entries", "Exits"])
ax.set_ylabel("Entries/exits per hour (1e6 is a million)")
ax.set_xlabel("Hour (0 is midnight, 12 is noon, 23 is 11pm)")
ax.set_xlim(0, 23)

turnstile_rain = turnstile_weather[["rain", "ENTRIESn_hourly", "EXITSn_hourly"]]
turnstile_rain["rain2"] = np.where(turnstile_rain["rain"] == 1, "raining", "not raining")
turnstile_rain.groupby("rain2").describe()

turnstile_rain = turnstile_weather[["rain", "ENTRIESn_hourly", "EXITSn_hourly"]]
turnstile_rain["ENTRIESn_hourly_log10"] = np.log10(turnstile_rain["ENTRIESn_hourly"] + 1)
turnstile_rain["rain2"] = np.where(turnstile_rain["rain"] == 1, "raining", "not raining")
set1 = brewer2mpl.get_map('Set1', 'qualitative', 3).mpl_colors
plot = gg.ggplot(turnstile_rain, gg.aes(x="ENTRIESn_hourly_log10", color="rain2")) + \
       gg.geom_density() + \
       gg.facet_wrap("rain2", scales="fixed") + \
       gg.scale_colour_manual(values=set1) + \
       gg.xlab("log10(entries per hour)") + \
       gg.ylab("Number of turnstiles") + \
       gg.ggtitle("Entries per hour whilst raining and not raining")
plot

np.random.seed(42)
data = pd.Series(np.random.normal(loc=180, scale=40, size=600))
data.hist()

p = turnstile_weather["ENTRIESn_hourly"].hist()
pylab.suptitle("Entries per hour across all stations")
pylab.xlabel("Entries per hour")
pylab.ylabel("Number of occurrences")

turnstile_weather["grp"]=turnstile_weather["rain"]+turnstile_weather["fog"]
plot=ggplot(aes(y='ENTRIESn_hourly',x='Hour'), data=turnstile_weather)+geom_histogram()+xlab("Hour")+ylab("ENTRIESn_hourly")+ggtitle("T")
print plot
