
n = "BROUHAHA"
x = 3 
y = 14
for i in n: 
  ascii =  ord(i) - ord ( 'A' ) 
  print ( ( x * ascii + y ) % 26 , end = "  " )