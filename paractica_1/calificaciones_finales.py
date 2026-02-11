#8,8,7,5,10,9,9,5,6,10
cal_final = [8,8,7,5,10,9,9,5,6,10]

suma_cal = 0

for i in cal_final:
    suma_cal += i
    promedio_cal = suma_cal/len(cal_final)

print(suma_cal)
print("promedio del grupo",promedio_cal)

reprovado=0
aprovado=0
for i in cal_final:
  if i <=5:
     reprovado = reprovado+1
  else:
     aprovado = aprovado+1
print("aprovados",aprovado)
print("porcentaje",(aprovado/len(cal_final))*100,"%")
print("reprovados",reprovado)
print("porcentaje",(reprovado/len(cal_final))*100,"%")

sobre_salientes = 0
for i in cal_final:
   if i >=8:
      sobre_salientes= sobre_salientes+1

print("Sobresaliente",sobre_salientes)