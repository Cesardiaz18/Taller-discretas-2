

n = int ( input ( "Ingrese numero: "))
resp = -1
for i in range ( 0 , n ):
  if ( i * i == n ):
    resp = i
    break
  if ( i * i > n ):
    break;
if( resp == -1 ):
  print ( "No es un numero cuadrado")
else:
  print ( "Es un numero cuadrado, y es cuadrado del numero" , i )



