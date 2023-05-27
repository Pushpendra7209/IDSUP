# -*- coding: utf-8 -*-
"""
Created on Sat May 27 16:20:42 2023

@author: hp
"""

from typing import List
Vector = List[float]

a = [6,7,8,9]
b = [1,2,3,4]


def add(v: Vector, w:Vector) -> Vector:
    assert len(v) == len(w)
    return [a+b for a,b in zip(v,w)]
print(add(a,b))



def sub(V: Vector, W: Vector) -> Vector:
    assert len(V) == len(W)
    return [a-b for a,b in zip(V,W)]
print(sub(a,b))



def mul(V: Vector, W: Vector) -> Vector:
    assert len(V) == len(W)
    return [a*b for a,b in zip(V,W)]
print(mul(a,b))


lst=[[1,2,3],[4,5,6],[6,7,8]]
def vector_sum(vectors: List[Vector]) -> Vector:
  assert vectors
  num_elements = len(vectors[0])
  assert all(len(v) == num_elements for v in vectors)
  return [sum(vector[i] for vector in vectors) for i in range(num_elements)]
print(vector_sum(lst))


def scalar_multiply(c: float, v: Vector) -> Vector:
  return [c * vi for vi in v]



def dot(v: Vector, w: Vector) -> float:
  assert len(v) == len(w)
  return sum(vi * wi for vi, wi in zip(v, w))
print('dot : -> ' , dot(a, b) )


def sum_of_squares(V: Vector) ->Vector:
    return dot(V, V)
print(sum_of_squares(b))




import math
def distance(V: Vector, W: Vector) -> Vector:
    assert len(V)  == len(W)
    return math.sqrt(Square_distance(V,W))

def Square_distance(V : Vector, W: Vector) -> Vector:
    return sum_of_squares(sub(V , W))
print('distance  -> ' ,distance(a,b))