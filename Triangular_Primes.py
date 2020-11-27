

import math
resp = True
for i in range ( 3 , 101 ): 
    triangular = int(i * ( i + 1 ) / 2) 
    prime = True
    for d in range ( 2 , int(math.sqrt(triangular)) + 2):
      if ( triangular % d == 0 ):
        prime = False 
    if ( prime == True ):
      resp = False
if ( resp == True ):
  print ( "Afirmacion correcta, los numeros triangulares de 3 a 100 no son primos")
else:
  print ( "Afirmacion falsa")

