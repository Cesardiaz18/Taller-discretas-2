
ciclo = True
for i in range ( 0 , 100 ):
  residuo = i**3 % 9
  if ( residuo == 8 ):
    residuo = -1 ; 
    if ( residuo % 3 == 0 and residuo != 0 ):
      ciclo = False
    if ( residuo % 3 == 1 and residuo != 1 ):
      ciclo = False
    if ( residuo % 3 == 2 and residuo != -1 ):
      ciclo = False
  print ( residuo , end = " " ) 
print ( ) ; 
if ( ciclo == True ):
  print ( "El patron persiste para los primeros 100 numeros")
else:
  print ( "El patron no persiste para los primeros 100 numeros")

