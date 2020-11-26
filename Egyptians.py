

a = int ( input ( "Ingrese numero a: " ) ) 
b = int ( input ( "Ingrese numero b: " ) ) 
cont = 0 ; 
for i in range ( 0 , a ): 
  list = [ b ] 
  for i in range ( 0 , cont ): 
    auxList = [ ] 
    for x in list:
      auxList.append ( x + 1 )
      auxList.append ( x * ( x + 1 ) ) 
    list = auxList 
  if ( len(list) == 1 ):
    print ( "1/" + str(b)  ,end="") ;  
  else:

    for x in list: 
      print ( "+1/" + str(x) ,end="")

  cont = cont + 1 ;

