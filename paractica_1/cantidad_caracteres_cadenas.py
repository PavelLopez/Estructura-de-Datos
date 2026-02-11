mi_cadena = "parangaricutirimicuaro"
mc_en_l = list(mi_cadena)
mc_may = list(mi_cadena.upper())

for i in mc_en_l:
    if mi_cadena.count(i)>0:
        print(i,'=',mc_en_l.count(i))

for i in mc_may:
    if mi_cadena.count(i)>0:
        print(i,'=',mc_en_l.count(i))