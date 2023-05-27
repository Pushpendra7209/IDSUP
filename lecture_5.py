# -*- coding: utf-8 -*-
"""
Created on Sat May 27 18:30:52 2023

@author: hp
"""

from collections import Counter
import matplotlib.pyplot as plt

num_friends = [100, 49, 41, 40, 25,20]
friend_counts = Counter(num_friends)
xs = range(101) #largest value is 100
ys = [friend_counts[x] for x in xs]
plt.bar(xs, ys)
plt.axis([0, 101, 0, 25]) #x-axis and y-axis limits
plt.title("Histogram of Friend Counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")
plt.show()


from typing import List
def mean(xs: List[float]) -> float:
   return sum(xs) / len(xs)
print(mean(num_friends))



odd = [2,5,1,3,4]
def median_odd(xs : List[float] ) -> float:
    return sorted(xs)[len(xs)//2]
print(median_odd(odd))


even = [8,5,7,3,6,2]
def median_even(xs: List[float]) ->  float:
     sorted_xs = sorted(xs)
     return (sorted_xs[(len(xs)//2-1) ] + sorted_xs[len(xs)//2])/2
print(median_even(even))


lst = [1,3,4,2,5,2,5,2,5]
def median(a : List[float])->float:
    a.sort()
    print(a)
    return median_even(lst) if len(lst) % 2 == 0 else median_odd(lst)
print(median(lst))


def quantile(xs : List[float], p : float) -> float:
  p_index = int(p * len(xs))
  return sorted(xs)[p_index]
print(quantile(lst,0.7))


def mode(a: List[float])->float:
    count = Counter(a)
    print(count)
    maximum = max(count.values())
    print(maximum)
    return [x for x ,c in count.items() if c == maximum]
print(mode(lst))