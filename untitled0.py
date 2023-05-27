# -*- coding: utf-8 -*-
"""
Created on Thu May 25 03:18:50 2023

@author: hp
"""


try:
   print(0 / 0)
except ZeroDivisionError:
   print("cannot divide by zero")
   



document = [1,12,32,4,2,1,3,1,3,1,2]
from collections import defaultdict
word_counts = defaultdict(int)
for word in document:
   word_counts[word] += 1
print(word_counts[1])

s = {}
t = set()

print(type(s))
print(type(t))



 
even = [x for x in range(5) if  x%2 == 0]
print(even)

even_square = [x*x for x in range(5) if x % 2 == 0]
print(even_square)

zeros = [0 for x in even]
print(zeros)

def smallest_item(xs):
   return min(xs)
assert smallest_item([10, 20, 5, 40]) == 5
print("hello")

from matplotlib import pyplot as plt
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7,
14958.3] 
plt.plot(years, gdp, color='orange', marker='o', linestyle='solid')
 
plt.title("Nominal GDP")
 
plt.ylabel("Billions of $")
plt.xlabel("Year")
plt.show()
plt.savefig()