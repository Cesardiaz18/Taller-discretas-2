

import math
for i in range ( 2 , 50 ):
  prime = True 
  for d in range ( 2 , int(math.sqrt ( i )) + 1):
    if ( i % d == 0 ):
      prime = False
  if ( prime == True ):
    resp = 0
    for d in range ( 1 , i ):
      resp = resp+ d**(i-1)
    print ( i,resp%i)

