# -*- coding: utf-8 -*-
"""
Created on Sat May 27 13:10:25 2023

@author: hp
"""
from matplotlib import pyplot as plt
year = [1950,1960,1970,1980,1990,2000,2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7,
14958.3]

plt.plot(year, gdp, color='blue', marker="o" , linestyle="dotted")

plt.title("nominal GDP")
plt.ylabel("$ in billions")
plt.xlabel("year")
plt.show()
plt.savefig()
