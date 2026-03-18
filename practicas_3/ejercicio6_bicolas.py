#simulacion de datos para reintento de tareas fallidas
#def procceso(Tareas):

class Tareas:
    def __init__(self,nombre,No_Fail_bf_Suc,No_ties):
        self.nombre = nombre
        self.No_Fail_bf_Suc = No_Fail_bf_Suc
        self.No_ties = No_ties

t1=Tareas("T1",1,0)
t2=Tareas("T2",0,0)
t3=Tareas("T3",2,0)
t4=Tareas("T4",1,0)
t5=Tareas("T5",2,2)
t6=Tareas("T6",2,1)