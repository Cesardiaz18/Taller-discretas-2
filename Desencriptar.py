# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CSCLsWeNFvN5rAyspi5MAmeqx8vTOsGY
"""

n = [ 14 , 10 , 6 , 22, 22 ]
x = 5
y = 10
inverse = 0  ;
for i in range ( 1 , 26 ): 
  if ( ( x * i ) % 26 == 1 ):
    inverse = i 
    break ; 
for i in n: 
  print ( chr( ( inverse * ( i - y )  % 26 ) + ord('A') )  , end = "" )