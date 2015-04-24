import scipy
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

turnstile_weather=pd.read_csv( "C:/move - bwlee/Data Analysis/Nano/\
Intro to Data Science/project/code/turnstile_data_master_with_weather.csv")

tbht = turnstile_weather[["Hour", "ENTRIESn_hourly", "rain"]]
#print tbht

#turnstile_by_hour.to_csv('dump.csv')
not_raining = turnstile_weather[turnstile_weather["rain"] == 0]
raining = turnstile_weather[turnstile_weather["rain"] == 1]
(u, pvalue) = scipy.stats.mannwhitneyu(not_raining["ENTRIESn_hourly"],
                                       raining["ENTRIESn_hourly"])
print "median entries per hour not raining: %s" % not_raining["ENTRIESn_hourly"].median()
print "median entries per hour raining: %s" % raining["ENTRIESn_hourly"].median()
print "mean entries per hour not raining: %s" % not_raining["ENTRIESn_hourly"].mean()
print "mean entries per hour raining: %s" % raining["ENTRIESn_hourly"].mean()
print "p-value of test statistic: %.4f" % (pvalue * 2, )
print "not raining size: ", not_raining["ENTRIESn_hourly"].shape
print "raining size: ", raining["ENTRIESn_hourly"].shape