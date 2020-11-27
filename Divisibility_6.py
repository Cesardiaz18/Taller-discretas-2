
resp = False
for i in range ( 0 , 1001 ):
  x = i ** 3 - i 
  if ( x % 6 != 0 ):
    print ( x )
    resp = True
    break
if ( resp == True ):
  print ( "Existe un numero que no es divisible en 6")
else:
  print ( "Afirmacion correcta , todos los numeros hasta 1000 cumplen la propiedad")

