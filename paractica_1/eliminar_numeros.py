#


x = [1,2,4,4,4,5,7,9,11,11,13,14,15,16,16]
#este es el mas sencillo usando las propiedades de python y los conjuntos
#y=set(x)
#print(y)

#este usa un solo arreglo
for i in range(len(x)-1,0,-1):
    if x[i] == x[i-1]:
        x.pop(i)
#este print es para ver que el recorrido se hace        
#    print(i)
print(x)

#este es con dos arreglos
#...
y = []