# -*- coding: utf-8 -*-
"""
Created on Sat May 27 15:08:08 2023

@author: hp
"""

from collections import Counter
from matplotlib import pyplot as plt
grades=[83, 35, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
 
histogram = Counter(min(grade // 10 * 10, 90) for grade in
grades)

print(histogram)

plt.bar([x+5 for x in histogram.keys()],
        histogram.values(), 10,
edgecolor="black") 
plt.axis([-5, 105, 0, 5])

plt.xticks([10 * i for i in range(11)])

plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution of Exam 1 Grades")
plt.show()
