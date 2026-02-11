#12,21,16,15,20,18,6,10,12,11,15,12
#Promedio.
#Sumar todos los datos del arreglo, dividirlo entre el total de elementos.
#Realizar una comparacion de todos los valores vs promedio
#Integrar un arreglo con todos los valores superiores al promedio
#Integrar un arrgelo con todos los valores inferiores  al promedio

tonelada_cereal = [12,21,16,15,20,18,6,10,12,11,15,12]

suma= 0 
for i in tonelada_cereal :
    suma += i
    promedio = suma/len(tonelada_cereal)

print(suma)
print("promedio anual",promedio)

menores=0
mayores=0
for i in tonelada_cereal:
    if i < promedio:
        menores+=1
    else :
        mayores = mayores+1

print("mayores al promedio",mayores)
print("menores al promedio",menores)