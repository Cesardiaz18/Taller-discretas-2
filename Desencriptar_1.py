

n = [ 22 , 8 , 11 , 22 , 9 ]
x = -9
y = 6
inverse = 0  ;
for i in range ( 1 , 26 ): 
  if ( ( x * i ) % 26 == 1 ):
    inverse = i 
    break ; 
for i in n: 
  print ( chr( ( inverse * ( i - y )  % 26 ) + ord('A') )  , end = "" )
