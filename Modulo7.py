
resp = True
for i in range ( 0 , 101 ):
  residuo = i**3 % 7
  if ( residuo == 6 ):
    residuo = -1 ; 
  if ( residuo != 0 and residuo != 1 and residuo !=-1 ):
    resp = False

if ( resp == True ):
  print ( "Para todos los numeros menores o iguales a 100, se cumple que el residuo modulo 7 del cubo de los numeros es igual a 0,1 o -1")
else:
  print ( "Para todos los numeros menores o iguales a 100, no se cumple que el residuo modulo 7 del cubo de los numeros es igual a 0,1 o -1")

