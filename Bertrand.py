import math
def Bertrand_postulate ( n ) :
  for i in range ( n , n*2 + 1): 
    if ( i == 1 ):
      continue 
    prime = True
    for d in range ( 2 , int(math.sqrt ( i )) + 1 ):
      if ( i % d == 0 ):
        prime = False
    if ( prime == True ) : 
      return i
  return -1 ; 
for i in range ( 2 , 1001 ):
  print ( Bertrand_postulate( i  ) )
