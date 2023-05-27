# -*- coding: utf-8 -*-
"""
Created on Fri May 26 00:01:23 2023

@author: hp
"""

def generate_range(n):
  i = 0
  while i < n:
   
   i += 1
   
   print(i)
  
   



lst =[3,4,5,6]


lst2=[4,5,6,7]
#print(list(enumerate(lst)))
#print(list(enumerate(lst2 , 6)))




import random

#random.seed(0)
#print(random.randrange(90))


#random.shuffle(lst)
#print(lst)

#print(random.choice(lst))

import re

target_string = "My name is maximums and my luck numbers are 12 45 78"
# split on white-space 
word_list = re.split("[am]", target_string)
#print(word_list)

ans = zip(lst,lst2)
#print(list(ans))

pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)
#print(letters, numbers)

def type_annotation(a:int,b:str()) -> str:
    return a+b
print(type_annotation(13,4))