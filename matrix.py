# -*- coding: utf-8 -*-
"""
Created on Sat May 27 17:50:57 2023

@author: hp
"""

from typing import Tuple,List
Matrix = Tuple[int,int]
def shape(A : Matrix ) ->Tuple[int,int]:
    row = len(A)
    col = len(A[0])
    return row,col

mat = [[1,2,3],[4,5,6],[7,8,9]]
print(shape(mat))



Vector = List[float]
#We can get the number of rows as follows:
def get_row(A: Matrix, i: int) -> Vector:
   return A[i]
print(get_row(mat, 1))

#We can get the number of columns as follows:
def get_column(A: Matrix, j: int) -> Vector:
   return [A_i[j] for A_i in A]
print(get_column(mat, 1))

